# -*- coding: utf-8 -*-

import os
import unittest
import subprocess

CLI_CLEVER = os.path.join(os.path.dirname(__file__), '../bin/clever ')

class CleverCLITestCase(unittest.TestCase):

  def run_clever(self, args='', env=None):
    """
    Runs the cli clever script, passes supplied args.
    """
    process = subprocess.Popen(CLI_CLEVER + args, shell=True, env=env,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    out, err = process.communicate()
    code = process.returncode
    return out, err, code

  def test_help(self):
    # Test help on error
    out, err, code = self.run_clever()
    self.assertEqual(code, 1)
    # Test help on option
    out, err, code = self.run_clever('-h')
    self.assertEqual(code, 0)

  def test_api_token(self):
    # Check for error when key is not provided
    out, err, code = self.run_clever('district all')
    self.assertEqual(code, 2)
    # Check for no error when key is provided via -t
    out, err, code = self.run_clever('district all -t DEMO_TOKEN')
    self.assertEqual(code, 0)
    # Check for no error when key is provided via CLEVER_API_TOKEN
    env = {'CLEVER_API_TOKEN':'DEMO_TOKEN'}
    out, err, code = self.run_clever('district all', env)
    self.assertEqual(code, 0)
