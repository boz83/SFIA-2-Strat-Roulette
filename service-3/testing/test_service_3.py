from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app


class TestBase(TestCase):
  def create_app(self):
    config_name = "testing"
    return app

  def setUp(self):
    pass

  def tearDown(self):
    pass


class TestService3(TestBase):
  def test_map_rule1(self):
    with patch('requests.get') as g:
      g.return_value.text = 'Dust 2'
      with patch('random.randrange') as r:
        r.return_value = 0
        response = self.client.post(
            url_for('get_rule'),
            data='Dust 2')
        self.assertIn(b'Gladiator: Only one person may leave spawn. When that person dies, the next person leaves', response.data)

  def test_map_rule2(self):
    with patch('requests.get') as g:
      g.return_value.text = 'Cobblestone'
      with patch('random.randrange') as r:
        r.return_value = 0
        response = self.client.post(
            url_for('get_rule'),
            data='Cobblestone')
        self.assertIn(b'Golden Gun: When the first person on your team gets a kill, everyone else must throw away their weapons and share the weapon that the first kill was made with (the golden gun)', response.data)
  
  def test_map_rule3(self):
    with patch('requests.get') as g:
      g.return_value.text = 'Inferno'
      with patch('random.randrange') as r:
        r.return_value = 0
        response = self.client.post(
            url_for('get_rule'),
            data='Inferno')
        self.assertIn(b'Juan Deag: All 5 buy deagles - Go juan or go home!', response.data)

  def test_map_rule4(self):
    with patch('requests.get') as g:
      g.return_value.text = 'Mirage'
      with patch('random.randrange') as r:
        r.return_value = 0
        response = self.client.post(
            url_for('get_rule'),
            data='Mirage')
        self.assertIn(b'Juan Taps Only: You may only fire 1 shot at a time. You must drop or reload your weapon before shooting again', response.data)
  
  def test_map_rule5(self):
    with patch('requests.get') as g:
      g.return_value.text = 'Cache'
      with patch('random.randrange') as r:
        r.return_value = 0
        response = self.client.post(
            url_for('get_rule'),
            data='Cache')
        self.assertIn(b'Clay Pigeon Shooting: Everyone buys a shotgun and must yell "PULL" whenever you fire at an enemy', response.data)
  
  def test_map_rule6(self):
    with patch('requests.get') as g:
      g.return_value.text = 'Vertigo'
      with patch('random.randrange') as r:
        r.return_value = 0
        response = self.client.post(
            url_for('get_rule'),
            data='Vertigo')
        self.assertIn(b'This is not a map in the active duty pool',response.data)