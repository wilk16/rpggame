import unittest
from ..characters.character import Character


class TestCharacterClass(unittest.TestCase):
	"""Tests for Character class"""
	
	def setUp(self):
		self.c = Character(name = 'Character_1')
		self.e = Character(name = 'Character_2')
	
	def test_basic_setup(self):
		"""Test initial values"""
		self.assertEqual(self.c.hp, self.c.max_hp)
		self.assertEqual(self.c.name, 'Character_1')
		
	def test_is_alive_method_when_dead(self):
		"""Should return 0"""
		self.c.set_hp(-self.c.hp)
		self.assertEqual(self.c.is_alive(), 0)
		
	def test_is_alive_method_when_alive(self):
		"""Should return 1, thus alive"""
		self.c.set_hp(self.c.max_hp)
		self.assertEqual(self.c.is_alive(), 1)

	def test_set_hp_method_when_healing_grater_that_max_hp(self):
		"""Healing should not exceed max_hp"""
		light_wound = 5
		self.c.hp = self.c.max_hp - light_wound
		before_healing = self.c.hp
		self.c.set_hp(10)
		after_healing = self.c.hp
		self.assertEqual(self.c.hp, self.c.max_hp)
		self.assertEqual(after_healing - before_healing, light_wound)

	# TODO: write these tests
	def test_set_hp_method_when_healing_less_that_max_hp(self):
		pass

	def test_set_hp_method_when_damage_kills(self):
		pass

	def test_set_hp_method_when_damage_not_kills(self):
		pass

	def test_set_mana_method_when_restoring_grater_that_max_mana(self):
		pass
		
	def test_set_mana_method_when_restoring_less_that_max_mana(self):
		pass

	def test_set_mana_method_when_reducing_to_less_than_zero(self):
		pass

	def test_set_mana_method_when_reducing_to_more_than_zero(self):
		pass

	def test_attack_enemy_method(self):
		pass
