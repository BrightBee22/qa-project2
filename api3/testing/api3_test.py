from application import app
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestAPI3(TestBase):
    def test_greatsword(self):
        with patch('random.randint') as w:
            w.return_value = 0
            response = self.client.get(url_for('get_weapon'))
            self.assertIn(b'Great Sword', response.data)

    def test_hammer(self):
        with patch('random.randint') as w:
            w.return_value = 1
            response = self.client.get(url_for('get_weapon'))
            self.assertIn(b'Hammer', response.data)
    
    def test_cb(self):
        with patch('random.randint') as m:
            m.return_value = 2
            response = self.client.get(url_for('get_weapon'))
            self.assertIn(b'Charge Blade', response.data)

    def test_ig(self):
        with patch('random.randint') as m:
            m.return_value = 3
            response = self.client.get(url_for('get_weapon'))
            self.assertIn(b'Insect Glaive', response.data)

    def test_bow(self):
        with patch('random.randint') as m:
            m.return_value = 4
            response = self.client.get(url_for('get_weapon'))
            self.assertIn(b'Bow', response.data)