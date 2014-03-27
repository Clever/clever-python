# -*- coding: utf-8 -*-
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import clever
from clever import importer
json = importer.import_json()

class CleverTestCase(unittest.TestCase):
  def setUp(self):
    super(CleverTestCase, self).setUp()
    clever.api_base = os.environ.get('CLEVER_API_BASE', 'https://api.clever.com')
    clever.api_key = 'DEMO_KEY'

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

  def test_unicode(self):
    # Make sure unicode requests can be sent
    self.assertRaises(clever.APIError, clever.District.retrieve, id=u'☃')

  def test_none_values(self):
    district = clever.District.all(sort=None)[0]
    self.assertTrue(district.id)

  def test_missing_id(self):
    district = clever.District()
    self.assertRaises(clever.InvalidRequestError, district.refresh)

class AuthenticationErrorTest(CleverTestCase):
  def test_invalid_credentials(self):
    key = clever.api_key
    try:
      clever.api_key = 'invalid'
      clever.District.all()
    except clever.AuthenticationError, e:
      self.assertEqual(401, e.http_status)
      self.assertTrue(isinstance(e.http_body, str))
      self.assertTrue(isinstance(e.json_body, dict))
    finally:
      clever.api_key = key

class InvalidRequestErrorTest(CleverTestCase):
  def test_nonexistent_object(self):
    try:
      clever.District.retrieve('invalid')
    except clever.APIError, e:
      self.assertEqual(404, e.http_status)
      self.assertFalse(isinstance(e.json_body, dict))  # 404 does not have a body
      self.assertTrue(isinstance(e.http_body, str))

if __name__ == '__main__':
  unittest.main()
