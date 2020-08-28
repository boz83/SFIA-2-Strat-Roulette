from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
  def create_app(self):
    config_name="testing"
    return app

class TestService1(TestBase):
  def test_get_map(self):
    response=self.client.get(url_for('get_map'))
    result=False
    for item in ['Dust 2', 'Cobblestone', 'Inferno', 'Mirage', 'Cache']:
      if bytes.decode(response.data) == item:
        result = True
    self.assertTrue(result)