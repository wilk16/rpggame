import unittest
from .map import *
from ..characters.hero import Hero
from ..misc.misc import msg_log

class TestHealthTileClass(unittest.TestCase):
	"""Tests for HealthTile class"""
	
	def setUp(self):
		self.h = Hero()
		self.t = HealthTile()
		
	def test_basic_setup(self):
		"""Test initial values"""
		self.assertEqual(self.t.symbol, '+')
		self.assertEqual(self.t.action, HealthTile.restore_health)
	
	def test_restore_health_method(self):
		"""Restore_health should restore heroe's full health"""
		self.h.hp = self.h.max_hp - 10
		self.t.action(hero = self.h)
		self.assertEqual(self.h.hp, self.h.max_hp)
		self.assertEqual(msg_log.message[-1], self.h.name +"'s full health was restored.")
		

class TestManaTileClass(unittest.TestCase):
	"""Tests for ManaTile class"""
	
	def setUp(self):
		self.h = Hero()
		self.t = ManaTile()
		
	def test_basic_setup(self):
		"""Test initial values"""
		self.assertEqual(self.t.symbol, 'm')
		self.assertEqual(self.t.action, ManaTile.restore_mana)
	
	def test_restore_mana_method(self):
		"""Restore_health should restore heroe's full mana"""
		self.h.mana = self.h.max_mana - 3
		self.t.action(hero = self.h)
		self.assertEqual(self.h.mana, self.h.max_mana)
		self.assertEqual(msg_log.message[-1], self.h.name +"'s full mana was restored.")

if __name__ == '__main__':
	unittest.main()
