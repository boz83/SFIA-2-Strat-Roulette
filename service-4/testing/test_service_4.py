import unittest
from flask import url_for
from unittest.mock import patch
from os import getenv
from flask_testing import TestCase
from application import app, db
from application.models import Strategys

class TestBase(TestCase):
  def create_app(self):
    app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
      SECRET_KEY=getenv('TEST_SECRET_KEY'),
      WTF_CSRF_ENABLED=False,
      DEBUG=True
      )
    return app
  
  def setUp(self):
    db.session.commit()
    db.drop_all()
    db.create_all()
    testStrategy=Strategys(map='Cache',strategy='Mid Rush',rule='Clay Pigeon Shooting: Everyone buys a shotgun and must yell "PULL" whenever you fire at an enemy')

    db.session.add(testStrategy)
    db.session.commit()

  def tearDown(self):
    db.session.remove()
    db.drop_all()

class TestService4(TestBase):

  def test_view_strategys(self):
    response=self.client.get(url_for('home'))
    self.assertEqual(response.status_code, 200)
  
  def test_view_new_strategy(self):
    response = self.client.get(url_for("generated_strats"))
    self.assertEqual(response.status_code, 200)