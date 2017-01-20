# -*- coding: utf-8 -*-

import os
import sys
import unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import clever
from clever import importer

class CleverTestCase(unittest.TestCase):
  def setUp(self):
    super(CleverTestCase, self).setUp()
    clever.set_token('DEMO_TOKEN')

class CertPinning(CleverTestCase):
  def test_prod_api(self):
    clever.api_base = 'https://api.clever.com'
    district = clever.District.all()[0]
    self.assertEqual(district.name, 'Demo District')

  def test_cert_failure(self):
    clever.api_base = 'https://httpbin.org'
    self.assertRaises(clever.APIConnectionError, clever.District.all)

if __name__ == '__main__':
  suite = unittest.TestSuite()
  suite.addTest(unittest.TestLoader().loadTestsFromTestCase(CertPinning))
  unittest.TextTestRunner(verbosity=2).run(suite)
