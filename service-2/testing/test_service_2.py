from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
  def create_app(self):
    config_name="testing"
    return app
  
  def setUp(self):
    pass
  
  def tearDown(self):
    pass
  

class TestService2(TestBase):
  def test_get_strat(self):
    response = self.client.get(url_for('get_strat'))
    result=False
    for strats in ['Bombsite A', 'Bombsite B', 'Mid Rush', 'Long Rush']:
      if bytes.decode(response.data) ==  strats:
        result=True
    self.assertTrue(result)