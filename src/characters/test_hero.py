import unittest
from unittest.mock import MagicMock
from .hero import *
from .monster import Vampire
from ..items.weapon import ShortSword, Weapon
from .character import Character


class TestFighterClass(unittest.TestCase):
	"""Tests for Fighter class"""
	
	def setUp(self):
		self.h = Fighter(name = 'Fight')
		self.e = Vampire()
		self.s = ShortSword()
		
	def test_basic_setup(self):
		"""Test initial values"""
		self.assertEqual(self.h.name, 'Fight')
		
	def test_bulk_up_method(self):
		"""Fighters attack should increase by 1"""
		old_attack = self.h.attack
		msg = self.h.bulk_up(self.e)
		self.assertEqual(self.h.attack - old_attack, 1)
		self.assertEqual(msg, self.h.name + "'s attack rose +1")
		
	def test_charge_method_with_no_mana(self):
		"""Should use normal attack instead"""
		self.h.mana = 0
		Character.attack_enemy = MagicMock(name = 'character.attack_enemy')
		msg = self.h.charge(self.e)
		self.assertEqual(self.h.mana, 0)
		self.assertEqual(self.h.equipment.weapon.die, self.s.die)
		Character.attack_enemy.assert_called_once_with(self.e)
		
	def test_charge_method_modify_weapon(self):
		"""Should call modify_weapon_die"""
		self.h.mana = self.h.max_mana
		Character.attack_enemy = MagicMock(name = 'character.attack_enemy')
		Weapon.modify_weapon_die = MagicMock(name = 'Weapon.modify_weapon_die')
		msg = self.h.charge(self.e)
		self.assertEqual(self.h.mana, self.h.max_mana - 1)
		Character.attack_enemy.assert_called_once_with(self.e)
		change_weapon = {'side_op': ADD, 'side_val': 0, 'amount_op': MUL, 'amount_val': 3}
		Weapon.modify_weapon_die.assert_called_once_with(**change_weapon)
		
	def test_charge_method_restore_weapon(self):
		"""Should call restore_weapon_die"""
		self.h.mana = self.h.max_mana
		Character.attack_enemy = MagicMock(name = 'character.attack_enemy')
		Weapon.restore_weapon_die = MagicMock(name = 'Weapon.restore_weapon_die')
		msg = self.h.charge(self.e)
		self.assertEqual(self.h.mana, self.h.max_mana - 1)
		Character.attack_enemy.assert_called_once_with(self.e)
		Weapon.restore_weapon_die.assert_called_once_with(die=self.s.die)
