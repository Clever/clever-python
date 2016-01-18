# -*- coding: utf-8 -*-
import os
import sys
import unittest
import urllib2
import httmock
import itertools

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import clever
from clever import importer
json = importer.import_json()

import requests
from httmock import response, HTTMock


def functional_test(auth):
  class FunctionalTests(CleverTestCase):

    def setUp(self):
      super(FunctionalTests, self).setUp()
      clever.api_base = os.environ.get('CLEVER_API_BASE', 'https://api.clever.com')
      if auth.get("token", None):
        clever.set_token(auth["token"])
      elif auth.get("api_key", None):
        clever.set_api_key(auth["api_key"])

    def test_dns_failure(self):
      api_base = clever.api_base
      try:
        clever.api_base = 'https://my-invalid-domain.ireallywontresolve/v1'
        self.assertRaises(clever.APIConnectionError, clever.District.all)
      finally:
        clever.api_base = api_base

    def test_list_accessors(self):
      district = clever.District.all()[0]
      self.assertEqual(district['name'], district.name)

    def test_starting_after(self):
      allevents = clever.Event.all()
      second_to_last_id = allevents[len(allevents)-2]['id']
      events = clever.Event.iter(starting_after=second_to_last_id)
      count = len(list(events))    
      self.assertTrue(count==1)

    def test_ending_before(self):
      allevents = clever.Event.all()
      second_id = allevents[1]['id']
      events = clever.Event.iter(ending_before=second_id)
      count = len(list(events))    
      self.assertTrue(count==1)

    def test_unicode(self):
      # Make sure unicode requests can be sent
      self.assertRaises(clever.APIError, clever.District.retrieve, id=u'☃')

    def test_none_values(self):
      district = clever.District.all(sort=None)[0]
      self.assertTrue(district.id)

    def test_missing_id(self):
      district = clever.District()
      self.assertRaises(clever.InvalidRequestError, district.refresh)
  return FunctionalTests


class CleverTestCase(unittest.TestCase):

  def setUp(self):
    super(CleverTestCase, self).setUp()
    clever.api_base = os.environ.get('CLEVER_API_BASE', 'https://api.clever.com')
    clever.set_api_key('DEMO_KEY')


class FunctionalTests(CleverTestCase):

  def test_dns_failure(self):
    api_base = clever.api_base
    try:
      clever.api_base = 'https://my-invalid-domain.ireallywontresolve/v1'
      self.assertRaises(clever.APIConnectionError, clever.District.all)
    finally:
      clever.api_base = api_base

  def test_list_accessors(self):
    district = clever.District.all()[0]
    self.assertEqual(district['name'], district.name)

  def test_iter(self):
    for district in clever.District.iter():
      self.assertTrue(district.id)

  def test_starting_after(self):
    allevents = clever.Event.all()
    second_to_last_id = allevents[len(allevents)-2]['id']
    events = clever.Event.iter(starting_after=second_to_last_id)
    count = len(list(events))    
    self.assertTrue(count==1)

  def test_ending_before(self):
    allevents = clever.Event.all()
    second_id = allevents[1]['id']
    events = clever.Event.iter(ending_before=second_id)
    count = len(list(events))    
    self.assertTrue(count==1)

  def test_iter_count(self):
      r = requests.get('https://api.clever.com/v1.1/students?count=true',
          headers={'Authorization': 'Bearer DEMO_TOKEN'})

      req_count = json.loads(r.text)["count"]
      iter_count = len([x for x in clever.Student.iter()])

      self.assertTrue(req_count > clever.Student.ITER_LIMIT)
      self.assertEqual(req_count, iter_count)

  def test_unsupported_params(self):
    self.assertRaises(clever.CleverError, lambda: clever.District.all(page=2))
    self.assertRaises(clever.CleverError, lambda: clever.District.all(limit=10))
    self.assertRaises(clever.CleverError, lambda: clever.District.all(page=2, limit=10))

  def test_unicode(self):
    # Make sure unicode requests can be sent
    self.assertRaises(clever.APIError, clever.District.retrieve, id=u'☃')

  def test_none_values(self):
    district = clever.District.all(sort=None)[0]
    self.assertTrue(district.id)

  def test_missing_id(self):
    district = clever.District()
    self.assertRaises(clever.InvalidRequestError, district.refresh)

  def test_keys_and_values_methods(self):
    clever_object = clever.CleverObject()
    self.assertEqual(clever_object.keys(), set())
    self.assertEqual(clever_object.values(), set())

  def test_empty_list_on_no_data(self):
    district = clever.District.all(where=json.dumps({'name': 'asdf'}))
    self.assertEqual(district, [])

  def _set_httplib_urllib2(self):
    clever.urllib2 = urllib2
    clever._httplib = 'urllib2'

  def test_pagination_urllib2(self):
    self._set_httplib_urllib2()
    teachers = clever.Teacher.all()
    clever.ListableAPIResource.ITER_LIMIT = 40
    self.assertTrue(len(teachers) > clever.ListableAPIResource.ITER_LIMIT,
                    msg='Invalid test - did not cross pagination threshold')

  def test_pagination_urllib2_with_params(self):
    self._set_httplib_urllib2()
    teachers = clever.Teacher.all(where='{"name.first": {"$gte": "A"}}')
    clever.ListableAPIResource.ITER_LIMIT = 40
    self.assertTrue(len(teachers) > clever.ListableAPIResource.ITER_LIMIT,
                    msg='Invalid test - did not cross pagination threshold')


class AuthenticationErrorTest(CleverTestCase):

  def test_invalid_credentials(self):
    key = clever.get_api_key()
    try:
      clever.set_api_key('invalid')
      clever.District.all()
    except clever.AuthenticationError, e:
      self.assertEqual(401, e.http_status)
      self.assertTrue(isinstance(e.http_body, str))
      self.assertTrue(isinstance(e.json_body, dict))
    finally:
      clever.set_api_key(key)


class InvalidRequestErrorTest(CleverTestCase):

  def test_nonexistent_object(self):
    try:
      clever.District.retrieve('invalid')
    except clever.APIError, e:
      self.assertEqual(404, e.http_status)
      self.assertFalse(isinstance(e.json_body, dict))  # 404 does not have a body
      self.assertTrue(isinstance(e.http_body, str))

#generates httmock responses for TooManyRequestsErrorTest
def too_many_requests_content(url, request):
  headers =  {
    'X-Ratelimit-Bucket': 'all, none',
    'X-Ratelimit-Limit' : '200, 1200',
    'X-Ratelimit-Reset' : '135136, 31634',
    'X-Ratelimit-Remaining' : '0, 0'
  }
  return response(429, "", headers, None, 5, None)

class TooManyRequestsErrorTest(CleverTestCase):

  def test_rate_limiter(self):
    with HTTMock(too_many_requests_content):
      r = requests.get('https://test.rate.limiting')
      res = {'body': r.content, 'headers': r.headers, 'code': 429}
      APIRequestor = clever.APIRequestor()
      self.assertRaises(clever.TooManyRequestsError, lambda : APIRequestor.interpret_response(res))

if __name__ == '__main__':
  suite = unittest.TestSuite()
  for TestClass in [
          functional_test({"api_key": "DEMO_KEY"}),
          functional_test({"token": "DEMO_TOKEN"}),
          AuthenticationErrorTest,
          InvalidRequestErrorTest,
          TooManyRequestsErrorTest]:
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestClass))
  unittest.TextTestRunner(verbosity=2).run(suite)

