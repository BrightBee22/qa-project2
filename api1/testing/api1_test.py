from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

class TestAPI1(TestBase):
    def test_bishaten_greatsword(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/monster', text ='Bishaten')
            m.get('http://service3:5002/get/weapon', text='Great Sword')
            m.post('http://service4:5003/post/recweapon', text='Bishaten,Great Sword')
            response = self.client.get(url_for('recweapon'))
            self.assertIn(b'Bishaten,Great Sword', response.data)

    def test_magnamalo_hammer(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/monster', text ='Magnamalo')
            m.get('http://service3:5002/get/weapon', text='Hammer')
            m.post('http://service4:5003/post/recweapon', text='Magnamalo,Hammer')
            response = self.client.get(url_for('recweapon'))
            self.assertIn(b'Magnamalo,Hammer', response.data)
    
    def test_rath_cb(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/monster', text ='Rathalos')
            m.get('http://service3:5002/get/weapon', text='Charge Blade')
            m.post('http://service4:5003/post/recweapon', text='Rathalos,Charge Blade')
            response = self.client.get(url_for('recweapon'))
            self.assertIn(b'Rathalos,Charge Blade', response.data)

    def test_val_ig(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/monster', text ='Valstrax')
            m.get('http://service3:5002/get/weapon', text='Insect Glaive')
            m.post('http://service4:5003/post/recweapon', text='Valstrax,Insect Glaive')
            response = self.client.get(url_for('recweapon'))
            self.assertIn(b'Valstrax,Insect Glaive', response.data)

    def test_cham_bow(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/monster', text ='Chameleos')
            m.get('http://service3:5002/get/weapon', text='Bow')
            m.post('http://service4:5003/post/recweapon', text='Chameleos,Bow')
            response = self.client.get(url_for('recweapon'))
            self.assertIn(b'Chameleos,Bow', response.data)