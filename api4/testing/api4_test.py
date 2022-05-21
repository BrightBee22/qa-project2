from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestAPI4(TestBase):
    def test_bishaten_greatsword(self):
        response = self.client.post(url_for('get_recweapon'), data='Bishaten,Great Sword')
        self.assertIn(b'Bishaten is weak to Ice, therefore I recommend the Abominable Great Sword (from the Goss Harag tree)', response.data)

    def test_bishaten_hammer(self):
        response = self.client.post(url_for('get_recweapon'), data='Bishaten,Hammer')
        self.assertIn(b'Bishaten is weak to Ice, therefore I recommend the Glacial Crunch (from the Barioth tree)', response.data)

    def test_bishaten_cb(self):
        response = self.client.post(url_for('get_recweapon'), data='Bishaten,Charge Blade')
        self.assertIn(b'Bishaten is weak to Ice, therefore I recommend the Pavadira (from the Barioth tree)', response.data)
    
    def test_bishaten_ig(self):
        response = self.client.post(url_for('get_recweapon'), data='Bishaten,Insect Glaive')
        self.assertIn(b'Bishaten is weak to Ice, therefore I recommend the Lagombavarice (from the Lagombi tree)', response.data)
    
    def test_bishaten_bow(self):
        response = self.client.post(url_for('get_recweapon'), data='Bishaten,Bow')
        self.assertIn(b'Bishaten is weak to Ice, therefore I recommend the Heavens Glaze (from the Ice tree)', response.data)

    def test_magnamalo_greatsword(self):
        response = self.client.post(url_for('get_recweapon'), data='Magnamalo,Great Sword')
        self.assertIn(b'Magnamalo is weak to Water, therefore I recommend the Akanesasu (from the Mizutsune tree)', response.data)

    def test_magnamalo_hammer(self):
        response = self.client.post(url_for('get_recweapon'), data='Magnamalo,Hammer')
        self.assertIn(b'Magnamalo is weak to Water, therefore I recommend the Doom Bringer Hammer (from the Almudron tree)', response.data)

    def test_magnamalo_cb(self):
        response = self.client.post(url_for('get_recweapon'), data='Magnamalo,Charge Blade')
        self.assertIn(b'Magnamalo is weak to Water, therefore I recommend the Final FieldBlade (from the Mizutsune tree)', response.data)
    
    def test_magnamalo_ig(self):
        response = self.client.post(url_for('get_recweapon'), data='Magnamalo,Insect Glaive')
        self.assertIn(b'Magnamalo is weak to Water, therefore I recommend the Watercolor Glaive (from the Smithy tree)', response.data)
    
    def test_magnamalo_bow(self):
        response = self.client.post(url_for('get_recweapon'), data='Magnamalo,Bow')
        self.assertIn(b'Magnamalo is weak to Water, therefore I recommend the Hail of Mud (from the Almudron tree)', response.data)

    def test_rathalos_greatsword(self):
        response = self.client.post(url_for('get_recweapon'), data='Rathalos,Great Sword')
        self.assertIn(b'Rathalos is weak to Thunder, therefore I recommend the Great Demon Rod (from the Rajang tree)', response.data)

    def test_rathalos_hammer(self):
        response = self.client.post(url_for('get_recweapon'), data='Rathalos,Hammer')
        self.assertIn(b'Rathalos is weak to Thunder, therefore I recommend the Super Nova (from the Thunder tree)', response.data)

    def test_rathalos_cb(self):
        response = self.client.post(url_for('get_recweapon'), data='Rathalos,Charge Blade')
        self.assertIn(b'Rathalos is weak to Thunder, therefore I recommend the Despots Thundergale (from the Zingore tree)', response.data)
    
    def test_rathalos_ig(self):
        response = self.client.post(url_for('get_recweapon'), data='Rathalos,Insect Glaive')
        self.assertIn(b'Rathalos is weak to Thunder, therefore I recommend the Full Bolt Chamber (from the Khezu tree)', response.data)
    
    def test_rathalos_bow(self):
        response = self.client.post(url_for('get_recweapon'), data='Rathalos,Bow')
        self.assertIn(b'Rathalos is weak to Thunder, therefore I recommend the Flying Kadachi Striker (from the Tobi-Kadachi tree)', response.data)

    def test_valstrax_greatsword(self):
        response = self.client.post(url_for('get_recweapon'), data='Valstrax,Great Sword')
        self.assertIn(b'Valstrax is weak to Blast, therefore I recommend the Sinister Shadeblade (from the Magnamalo tree)', response.data)

    def test_valstrax_hammer(self):
        response = self.client.post(url_for('get_recweapon'), data='Valstrax,Hammer')
        self.assertIn(b'Valstrax is weak to Blast, therefore I recommend the Teostra Cratergouger (from the Teostra tree)', response.data)

    def test_valstrax_cb(self):
        response = self.client.post(url_for('get_recweapon'), data='Valstrax,Charge Blade')
        self.assertIn(b'Valstrax is weak to Blast, therefore I recommend the Sinister Shade Axe (from the Magnamalo tree)', response.data)
    
    def test_valstrax_ig(self):
        response = self.client.post(url_for('get_recweapon'), data='Valstrax,Insect Glaive')
        self.assertIn(b'Valstrax is weak to Blast, therefore I recommend the Sinister Shadowstaff (from the Magnamalo tree)', response.data)
    
    def test_valstrax_bow(self):
        response = self.client.post(url_for('get_recweapon'), data='Valstrax,Bow')
        self.assertIn(b'Valstrax is weak to Blast, therefore I recommend the Bow of Light & Courage (from the Teostra tree)', response.data)
    
    def test_chameleos_greatsword(self):
        response = self.client.post(url_for('get_recweapon'), data='Chameleos,Great Sword')
        self.assertIn(b'Chameleos is weak to Fire, therefore I recommend the Rathalos Firesword (from the Rathalos tree)', response.data)

    def test_chameleos_hammer(self):
        response = self.client.post(url_for('get_recweapon'), data='Chameleos,Hammer')
        self.assertIn(b'Chameleos is weak to Fire, therefore I recommend the Pheonix Fury (from the Anjanath tree)', response.data)

    def test_chameleos_cb(self):
        response = self.client.post(url_for('get_recweapon'), data='Chameleos,Charge Blade')
        self.assertIn(b'Chameleos is weak to Fire, therefore I recommend the Biting Edge II (from the Rakna-Kadaki tree)', response.data)
    
    def test_chameleos_ig(self):
        response = self.client.post(url_for('get_recweapon'), data='Chameleos,Insect Glaive')
        self.assertIn(b'Chameleos is weak to Fire, therefore I recommend the Rielle Vermiglio (from the Bnahabra tree)', response.data)
    
    def test_chameleos_bow(self):
        response = self.client.post(url_for('get_recweapon'), data='Chameleos,Bow')
        self.assertIn(b'Chameleos is weak to Fire, therefore I recommend the Dark Filament (from the Rathalos tree)', response.data)
    


    
