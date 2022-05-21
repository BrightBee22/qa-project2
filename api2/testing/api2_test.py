from application import app
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestAPI2(TestBase):
    def test_bishaten(self):
        with patch('random.randint') as m:
            m.return_value = 0
            response = self.client.get(url_for('get_monster'))
            self.assertIn(b'Bishaten', response.data)

    def test_magnamalo(self):
        with patch('random.randint') as m:
            m.return_value = 1
            response = self.client.get(url_for('get_monster'))
            self.assertIn(b'Magnamalo', response.data)
    
    def test_rath(self):
        with patch('random.randint') as m:
            m.return_value = 2
            response = self.client.get(url_for('get_monster'))
            self.assertIn(b'Rathalos', response.data)

    def test_val(self):
        with patch('random.randint') as m:
            m.return_value = 3
            response = self.client.get(url_for('get_monster'))
            self.assertIn(b'Valstrax', response.data)

    def test_cham(self):
        with patch('random.randint') as m:
            m.return_value = 4
            response = self.client.get(url_for('get_monster'))
            self.assertIn(b'Chameleos', response.data)