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
  

class TestService1(TestBase):
  def test_get_map(self):
    response=self.client.get(url_for('get_map'))
    result=False
    for maps in ['Dust 2', 'Cobblestone', 'Inferno', 'Mirage', 'Cache']:
      if bytes.decode(response.data) == maps:
        result = True
    self.assertTrue(result)