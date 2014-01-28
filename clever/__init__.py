# Clever Python bindings
# API docs at https://clever.com/developers/docs
# Author: Rafael Garcia
# Borrows heavily from the Python bindings for the Stripe API

## Imports
import logging
import os
import platform
import sys
import urllib
import textwrap
import time
import datetime
import types
import base64
import pkg_resources

# Use cStringIO if ita's available.  Otherwise, StringIO is fine.
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

# - Requests is the preferred HTTP library
# - Google App Engine has urlfetch
# - Use Pycurl if it's there (at least it verifies SSL certs)
# - Fall back to urllib2 with a warning if needed
_httplib = None

try:
  from google.appengine.api import urlfetch
  _httplib = 'urlfetch'
except ImportError:
  pass

if not _httplib:
  try:
    import requests
    _httplib = 'requests'
  except ImportError:
    pass

  try:
    # Require version 0.8.8, but don't want to depend on distutils
    version = requests.__version__
    major, minor, patch = [int(i) for i in version.split('.')]
  except:
    # Probably some new-fangled version, so it should support verify
    pass
  else:
    if major == 0 and (minor < 8 or (minor == 8 and patch < 8)):
      print >>sys.stderr, 'Warning: the Clever library requires that your Python "requests" library has a version no older than 0.8.8, but your "requests" library has version %s. Clever will fall back to an alternate HTTP library, so everything should work, though we recommend upgrading your "requests" library. If you have any questions, please contact support@clever.com. (HINT: running "pip install -U requests" should upgrade your requests library to the latest version.)' % (version, )
      _httplib = None

if not _httplib:
  try:
    import pycurl
    _httplib = 'pycurl'
  except ImportError:
    pass

if not _httplib:
  try:
    import urllib2
    _httplib = 'urllib2'
    print >>sys.stderr, "Warning: the Clever library is falling back to urllib2 because pycurl isn't installed. urllib2's SSL implementation doesn't verify server certificates. For improved security, we suggest installing pycurl."
  except ImportError:
    pass

if not _httplib:
  raise ImportError("Clever requires one of pycurl, Google App Engine's urlfetch, or urllib2.  If you are on a platform where none of these libraries are available, please let us know at support@clever.com.")

from version import VERSION
import importer
json = importer.import_json()

logger = logging.getLogger('clever')

# Use certs chain bundle including in the package for SSL verification
CLEVER_CERTS = pkg_resources.resource_filename(__name__, 'data/clever.com_ca_bundle.crt')

## Configuration variables

api_key = None
api_base = 'https://api.clever.com'
verify_ssl_certs = True

## Exceptions
class CleverError(Exception):
  def __init__(self, message=None, http_body=None, http_status=None, json_body=None):
    super(CleverError, self).__init__(message)
    self.http_body = http_body
    self.http_status = http_status
    self.json_body = json_body

class APIError(CleverError):
  pass

class APIConnectionError(CleverError):
  pass

class InvalidRequestError(CleverError):
  def __init__(self, message, http_body=None, http_status=None, json_body=None):
    super(InvalidRequestError, self).__init__(message, http_body, http_status, json_body)

class AuthenticationError(CleverError):
  pass

def convert_to_clever_object(klass, resp, api_key):
  # TODO: to support includes we'll have to infer klass from resp['uri']
  if isinstance(resp, dict) and resp.get('data', None):
    if isinstance(resp['data'], list):
      return [convert_to_clever_object(klass, i, api_key) for i in resp['data']]
    elif isinstance(resp['data'], dict):
      return klass.construct_from(resp['data'].copy(), api_key)
  elif isinstance(resp, basestring) or isinstance(resp, list) or isinstance(resp, dict) or isinstance(resp, bool):
    return resp
  else:
    raise Exception('DONT KNOW WHAT TO DO WITH {0}'.format(resp))

# makes it easier to update a nested key in a dict
def put(d, keys, item):
  if "." in keys:
    key, rest = keys.split(".", 1)
    if key not in d:
      d[key] = {}
    put(d[key], rest, item)
  else:
    d[keys] = item

## Network transport
class APIRequestor(object):
  def __init__(self, key=None):
    self._api_key = key

  @classmethod
  def api_url(cls, path=''):
    return '%s%s' % (api_base, path)

  @classmethod
  def _utf8(cls, value):
    if isinstance(value, unicode):
      return value.encode('utf-8')
    else:
      return value

  @classmethod
  def _objects_to_ids(cls, d):
    if isinstance(d, APIResource):
      return d.id
    elif isinstance(d, dict):
      res = {}
      for k, v in d.iteritems():
        res[k] = cls._objects_to_ids(v)
      return res
    else:
      return d

  @classmethod
  def urlencode(cls, d):
    """
    Internal: encode a dict for url representation
    If we ever need fancy encoding of embedded objects do it here
    """
    return urllib.urlencode(d)

  @classmethod
  def jsonencode(cls, d):
    """
    Internal: encode a dict for a post/patch body
    """
    return json.dumps(d)

  def request(self, meth, url, params={}):
    rbody, rcode, my_api_key = self.request_raw(meth, url, params)
    resp = self.interpret_response(rbody, rcode)
    return resp, my_api_key

  def handle_api_error(self, rbody, rcode, resp):
    try:
      error = resp['error']
    except (KeyError, TypeError):
      raise APIError("Invalid response object from API: %r (HTTP response code was %d)" % (rbody, rcode), rbody, rcode, resp)

    if rcode in [400]:
      raise InvalidRequestError(error, rbody, rcode, resp)
    elif rcode == 401:
      raise AuthenticationError(error, rbody, rcode, resp)
    else:
      raise APIError(error, rbody, rcode, resp)

  def request_raw(self, meth, url, params={}):
    """
    Mechanism for issuing an API call
    """
    my_api_key = self._api_key or api_key
    if my_api_key is None:
      raise AuthenticationError('No API key provided. (HINT: set your API key using "clever.api_key = <API-KEY>"). You can generate API keys from the Clever web interface.  See https://clever.com/api for details, or email support@clever.com if you have any questions.')

    abs_url = self.api_url(url)
    params = params.copy()
    self._objects_to_ids(params)

    ua = {
      'bindings_version' : VERSION,
      'lang' : 'python',
      'publisher' : 'clever'
      }
    for attr, func in [['lang_version', platform.python_version],
                       ['platform', platform.platform],
                       ['uname', lambda: ' '.join(platform.uname())]]:
      try:
        val = func()
      except Exception, e:
        val = "!! %s" % e
      ua[attr] = val

    headers = {
      'X-Clever-Client-User-Agent' : json.dumps(ua),
      'User-Agent' : 'Clever/v1.1 PythonBindings/%s' % (VERSION, ),
      'Authorization' : 'Basic %s:' % (base64.b64encode(my_api_key), )
      }
    if _httplib == 'requests':
      rbody, rcode = self.requests_request(meth, abs_url, headers, params)
    elif _httplib == 'pycurl':
      rbody, rcode = self.pycurl_request(meth, abs_url, headers, params)
    elif _httplib == 'urlfetch':
      rbody, rcode = self.urlfetch_request(meth, abs_url, headers, params)
    elif _httplib == 'urllib2':
      rbody, rcode = self.urllib2_request(meth, abs_url, headers, params)
    else:
      raise CleverError("Clever Python library bug discovered: invalid httplib %s.  Please report to support@clever.com" % (_httplib, ))
    logger.debug('API request to %s returned (response code, response body) of (%d, %r)' % (abs_url, rcode, rbody))
    return rbody, rcode, my_api_key

  def interpret_response(self, rbody, rcode):
    try:
      resp = json.loads(rbody)
    except Exception:
      raise APIError("Invalid response body from API: %s (HTTP response code was %d)" % (rbody, rcode), rbody, rcode)
    if not (200 <= rcode < 300):
      self.handle_api_error(rbody, rcode, resp)
    return resp

  def requests_request(self, meth, abs_url, headers, params):
    meth = meth.lower()
    if meth == 'get' or meth == 'delete':
      if params:
          abs_url = '%s?%s' % (abs_url, self.urlencode(params))
      data = None
    elif meth in ['post', 'patch']:
      data = self.jsonencode(params)
      headers['Content-Type'] = 'application/json'
    else:
      raise APIConnectionError('Unrecognized HTTP method %r.  This may indicate a bug in the Clever bindings.  Please contact support@clever.com for assistance.' % (meth, ))

    try:
      try:
        # Use a CA_BUNDLE containing the following chain:
        # - TrustedRoot
        # - DigiCert High Assurance EV - 1
        # - Clever.com EV
        # 
        # This ensures that only this certificate chain is used to verify SSL certs. 
        # Certs dervived from other ca certs will be treated as invalid.
        # eg. https://api.twitter.com and https://api.stripe.com FAIL
        #     https://api.clever.com and https://api.github.com PASS 
        # 
        # TODO: This gets us close to CERT PINNING but we need to pin the entire chain not just the CA
        result = requests.request(meth, abs_url,
                                  headers=headers, data=data, timeout=80,
                                  verify=CLEVER_CERTS)
      except TypeError, e:
        raise TypeError('Warning: It looks like your installed version of the "requests" library is not compatible with Clever\'s usage thereof. (HINT: The most likely cause is that your "requests" library is out of date. You can fix that by running "pip install -U requests".) The underlying error was: %s' %(e, ))

      # This causes the content to actually be read, which could cause
      # e.g. a socket timeout. TODO: The other fetch methods probably
      # are succeptible to the same and should be updated.
      content = result.content
      status_code = result.status_code
    except Exception, e:
      # Would catch just requests.exceptions.RequestException, but can
      # also raise ValueError, RuntimeError, etc.
      self.handle_requests_error(e)
    return content, status_code

  def handle_requests_error(self, e):
    if isinstance(e, requests.exceptions.RequestException):
      msg = "Unexpected error communicating with Clever.  If this problem persists, let us know at support@clever.com."
      err = "%s: %s" % (type(e).__name__, e.message)
    else:
      msg = "Unexpected error communicating with Clever.  It looks like there's probably a configuration issue locally.  If this problem persists, let us know at support@clever.com."
      err = "A %s was raised" % (type(e).__name__, )
      if e.message:
        err += " with error message %s" % (e.message, )
      else:
        err += " with no error message"
    msg = textwrap.fill(msg) + "\n\n(Network error: " + err + ")"
    raise APIConnectionError(msg)

  def pycurl_request(self, meth, abs_url, headers, params):
    s = StringIO.StringIO()
    curl = pycurl.Curl()

    meth = meth.lower()
    if meth == 'get':
      curl.setopt(pycurl.HTTPGET, 1)
      # TODO: maybe be a bit less manual here
      if params:
        abs_url = '%s?%s' % (abs_url, self.urlencode(params))
    elif meth in ['post', 'patch']:
      curl.setopt(pycurl.POST, 1)
      curl.setopt(pycurl.POSTFIELDS, self.jsonencode(params))
      headers['Content-Type'] = 'application/json'
    elif meth == 'delete':
      curl.setopt(pycurl.CUSTOMREQUEST, 'DELETE')
      if params:
        raise APIConnectionError("Did not expect params in DELETE request")
    else:
      raise APIConnectionError('Unrecognized HTTP method %r.  This may indicate a bug in the Clever bindings.  Please contact support@clever.com for assistance.' % (meth, ))

    # pycurl doesn't like unicode URLs
    abs_url = self._utf8(abs_url)
    curl.setopt(pycurl.URL, abs_url)
    curl.setopt(pycurl.WRITEFUNCTION, s.write)
    curl.setopt(pycurl.NOSIGNAL, 1)
    curl.setopt(pycurl.CONNECTTIMEOUT, 30)
    curl.setopt(pycurl.TIMEOUT, 80)
    curl.setopt(pycurl.HTTPHEADER, ['%s: %s' % (k, v) for k, v in headers.iteritems()])
    if verify_ssl_certs:
      curl.setopt(pycurl.CAINFO, CLEVER_CERTS)
    else:
      curl.setopt(pycurl.SSL_VERIFYHOST, False)

    try:
      curl.perform()
    except pycurl.error, e:
      self.handle_pycurl_error(e)
    rbody = s.getvalue()
    rcode = curl.getinfo(pycurl.RESPONSE_CODE)
    return rbody, rcode

  def handle_pycurl_error(self, e):
    if e[0] in [pycurl.E_COULDNT_CONNECT,
                pycurl.E_COULDNT_RESOLVE_HOST,
                pycurl.E_OPERATION_TIMEOUTED]:
      msg = "Could not connect to Clever (%s).  Please check your internet connection and try again.  If this problem persists, you should check Clever's service status at http://status.clever.com, or let us know at support@clever.com." % (api_base, )
    elif e[0] == pycurl.E_SSL_CACERT or e[0] == pycurl.E_SSL_PEER_CERTIFICATE:
      msg = "Could not verify Clever's SSL certificate.  Please make sure that your network is not intercepting certificates.  (Try going to %s in your browser.)  If this problem persists, let us know at support@clever.com." % (api_base, )
    else:
      msg = "Unexpected error communicating with Clever.  If this problem persists, let us know at support@clever.com."
    msg = textwrap.fill(msg) + "\n\n(Network error: " + e[1] + ")"
    raise APIConnectionError(msg)

  def urlfetch_request(self, meth, abs_url, headers, params):
    args = {}
    if meth == 'get':
      abs_url = '%s?%s' % (abs_url, self.urlencode(params))
    elif meth in ['post', 'patch']:
      args['payload'] = self.jsonencode(params)
      headers['Content-Type'] = 'application/json'
    elif meth == 'delete':
      if params:
        raise APIConnectionError("Did not expect params in DELETE request")
    else:
      raise APIConnectionError('Unrecognized HTTP method %r.  This may indicate a bug in the Clever bindings.  Please contact support@clever.com for assistance.' % (meth, ))
    args['url'] = abs_url
    args['method'] = meth
    args['headers'] = headers
    # Google App Engine doesn't let us specify our own cert bundle.
    # However, that's ok because the CA bundle they use recognizes
    # api.clever.com.
    args['validate_certificate'] = verify_ssl_certs
    # GAE requests time out after 60 seconds, so make sure we leave
    # some time for the application to handle a slow Clever
    args['deadline'] = 55

    try:
      result = urlfetch.fetch(**args)
    except urlfetch.Error, e:
      self.handle_urlfetch_error(e, abs_url)
    return result.content, result.status_code

  def handle_urlfetch_error(self, e, abs_url):
    if isinstance(e, urlfetch.InvalidURLError):
      msg = "The Clever library attempted to fetch an invalid URL (%r).  This is likely due to a bug in the Clever Python bindings.  Please let us know at support@clever.com." % (abs_url, )
    elif isinstance(e, urlfetch.DownloadError):
      msg = "There were a problem retrieving data from Clever."
    elif isinstance(e, urlfetch.ResponseTooLargeError):
      msg = "There was a problem receiving all of your data from Clever.  This is likely due to a bug in Clever.  Please let us know at support@clever.com."
    else:
      msg = "Unexpected error communicating with Clever.  If this problem persists, let us know at support@clever.com."
    msg = textwrap.fill(msg) + "\n\n(Network error: " + str(e) + ")"
    raise APIConnectionError(msg)

  def urllib2_request(self, meth, abs_url, headers, params):
    args = {}
    if meth == 'get':
      abs_url = '%s?%s' % (abs_url, self.urlencode(params))
      req = urllib2.Request(abs_url, None, headers)
    elif meth in ['post', 'patch']:
      body = self.jsonencode(params)
      headers['Content-Type'] = 'application/json'
      req = urllib2.Request(abs_url, body, headers)
      if meth == 'patch':
        req.get_method = lambda: 'PATCH'
    elif meth == 'delete':
      req = urllib2.Request(abs_url, None, headers)
      req.get_method = lambda: 'DELETE'
      if params:
        raise APIConnectionError("Did not expect params in DELETE request")
    else:
      raise APIConnectionError('Unrecognized HTTP method %r.  This may indicate a bug in the Clever bindings.  Please contact support@clever.com for assistance.' % (meth, ))

    try:
      response = urllib2.urlopen(req)
      rbody = response.read()
      rcode = response.code
    except urllib2.HTTPError, e:
      rcode = e.code
      rbody = e.read()
    except (urllib2.URLError, ValueError), e:
      self.handle_urllib2_error(e, abs_url)
    return rbody, rcode

  def handle_urllib2_error(self, e, abs_url):
    msg = "Unexpected error communicating with Clever.  If this problem persists, let us know at support@clever.com."
    msg = textwrap.fill(msg) + "\n\n(Network error: " + str(e) + ")"
    raise APIConnectionError(msg)


class CleverObject(object):
  _permanent_attributes = set(['_api_key'])

  # Adding these to enable pickling
  # http://docs.python.org/2/library/pickle.html#pickling-and-unpickling-normal-class-instances
  def __getstate__(self):
    return self.__dict__

  def __setstate__(self, d):
    self.__dict__.update(d)

  def __init__(self, id=None, api_key=None):
    self.__dict__['_values'] = set()
    self.__dict__['_unsaved_values'] = set()
    self.__dict__['_transient_values'] = set()
    self.__dict__['_api_key'] = api_key

    if id:
      self.id = id

  def __setattr__(self, k, v):
    # if in dot notation, insert into _unsaved_values the key in dot notation. this will cause it to be properly PATCHed.
    # remove these values when resetting state in refresh_from()
    # also make correct update to _values and __dict__ dicts so that state is correct
    # the end effect is that we can PATCH things in dot notation for selective updating of a system object
    if '.' in k:
      put(self.__dict__, k, v)
      self._values.add(k.split('.', 1)[0])
      self._unsaved_values.add(k)
    else:
      self.__dict__[k] = v
      self._values.add(k)
      if k not in self._permanent_attributes:
        self._unsaved_values.add(k)

  def __getattr__(self, k, obj=None):
    if obj == None: obj = self.__dict__
    if '.' in k:
      key, rest = k.split('.', 1)
      return self.__getattr__(rest, obj[key])
    else:
      try:
        return obj[k]
      except KeyError:
        pass
      if k in self._transient_values:
        raise AttributeError("%r object has no attribute %r.  HINT: The %r attribute was set in the past, however.  It was then wiped when refreshing the object with the result returned by Clever's API, probably as a result of a save().  The attributes currently available on this object are: %s" %
                             (type(self).__name__, k, k, ', '.join(self._values)))
      else:
        raise AttributeError("%r object has no attribute %r" % (type(self).__name__, k))

  def __getitem__(self, k):
    if k in self._values:
      return self.__dict__[k]
    elif k in self._transient_values:
      raise KeyError("%r.  HINT: The %r attribute was set in the past, however.  It was then wiped when refreshing the object with the result returned by Clever's API, probably as a result of a save().  The attributes currently available on this object are: %s" % (k, k, ', '.join(self._values)))
    else:
      raise KeyError(k)

  def get(self, k, default=None):
    try:
      return self[k]
    except KeyError:
      return default

  def setdefault(self, k, default=None):
    try:
      return self[k]
    except KeyError:
      self[k] = default
      return default

  def __setitem__(self, k, v):
    setattr(self, k, v)

  def keys(self):
    return self._values.keys()

  def values(self):
    return self._values.keys()

  @classmethod
  def construct_from(cls, values, api_key):
    instance = cls(values.get('id'), api_key)
    instance.refresh_from(values, api_key)
    return instance

  def refresh_from(self, values, api_key, partial=False):
    self._api_key = api_key

    # Wipe old state before setting new.  This is useful for e.g. updating a
    # customer, where there is no persistent card parameter.  Mark those values
    # which don't persist as transient
    if partial:
      removed = set()
    else:
      removed = self._values - set(values)

    for k in list(self._unsaved_values):
      if '.' in k:
        self._unsaved_values.discard(k)

    for k in removed:
      if k in self._permanent_attributes:
        continue
      del self.__dict__[k]
      self._values.discard(k)
      self._transient_values.add(k)
      self._unsaved_values.discard(k)

    for k, v in values.iteritems():
      if k in self._permanent_attributes:
        continue
      self.__dict__[k] = convert_to_clever_object(self, v, api_key)
      self._values.add(k)
      self._transient_values.discard(k)
      self._unsaved_values.discard(k)

  def __repr__(self):
    id_string = ''
    if isinstance(self.get('id'), basestring):
      id_string = ' id=%s' % self.get('id').encode('utf8')

    return '<%s%s at %s> JSON: %s' % (type(self).__name__, id_string, hex(id(self)), json.dumps(self.to_dict(), sort_keys=True, indent=2, cls=CleverObjectEncoder))

  def __str__(self):
    return json.dumps(self.to_dict(), sort_keys=True, indent=2, cls=CleverObjectEncoder)

  def to_dict(self):
    def _serialize(o):
      if isinstance(o, CleverObject):
        return o.to_dict()
      if isinstance(o, list):
        return [_serialize(i) for i in o]
      return o

    d = dict()
    for k in sorted(self._values):
      if k in self._permanent_attributes:
        continue
      v = getattr(self, k)
      v = _serialize(v)
      d[k] = v
    return d

class CleverObjectEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, CleverObject):
      return obj.to_dict()
    else:
      return json.JSONEncoder.default(self, obj)

class APIResource(CleverObject):
  def _ident(self):
    return [self.get('id')]

  @classmethod
  def retrieve(cls, id, api_key=None):
    instance = cls(id, api_key)
    instance.refresh()
    return instance

  def refresh(self):
    requestor = APIRequestor(self._api_key)
    url = self.instance_url()
    response, api_key = requestor.request('get', url)
    self.refresh_from(response['data'], api_key)
    return self

  @classmethod
  def class_name(cls):
    if cls == APIResource:
      raise NotImplementedError('APIResource is an abstract class.  You should perform actions on its subclasses (Charge, Customer, etc.)')
    return "%s" % urllib.quote_plus(cls.__name__.lower())

  @classmethod
  def class_url(cls):
    cls_name = cls.class_name()
    return "/v1.1/%ss" % cls_name

  def instance_url(self):
    id = self.get('id')
    if not id:
      raise InvalidRequestError('Could not determine which URL to request: %s instance has invalid ID: %r' % (type(self).__name__, id), 'id')
    id = APIRequestor._utf8(id)
    base = self.class_url()
    extn = urllib.quote_plus(id)
    return "%s/%s" % (base, extn)

# Classes of API operations
class ListableAPIResource(APIResource):
  @classmethod
  def all(cls, api_key=None, **params):
    requestor = APIRequestor(api_key)
    url = cls.class_url()
    response, api_key = requestor.request('get', url, params)
    return convert_to_clever_object(cls, response, api_key)

class CreatableAPIResource(APIResource):
  @classmethod
  def create(cls, api_key=None, **params):
    requestor = APIRequestor(api_key)
    url = cls.class_url()
    response, api_key = requestor.request('post', url, params)
    return convert_to_clever_object(cls, response, api_key)

class UpdateableAPIResource(APIResource):
  def save(self):
    if self._unsaved_values:
      requestor = APIRequestor(self._api_key)
      params = {}
      for k in self._unsaved_values:
        params[k] = getattr(self, k)
      url = self.instance_url()
      response, api_key = requestor.request('patch', url, params)
      self.refresh_from(response['data'], api_key)
    else:
      logger.debug("Trying to save already saved object %r" % (self, ))
    return self

class DeletableAPIResource(APIResource):
  def delete(self, **params):
    requestor = APIRequestor(self._api_key)
    url = self.instance_url()
    response, api_key = requestor.request('delete', url, params)
    self.refresh_from(response['data'], api_key)
    return self

# API objects
class District(ListableAPIResource):
  pass

class School(ListableAPIResource):
  pass

class Section(ListableAPIResource):
  pass

class Student(ListableAPIResource):
  pass

class Teacher(ListableAPIResource):
  pass

class Event(ListableAPIResource):
  pass
