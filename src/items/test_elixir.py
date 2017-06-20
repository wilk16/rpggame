import unittest
from .elixir import Elixir, HealingPotion, ManaPotion
from ..characters.hero import Hero


class TestElixirClass(unittest.TestCase):
	"""Tests for Elixir class"""
	def setUp(self):
		self.e = Elixir()
		self.h = Hero()
		
	def test_basic_setup(self):
		"""Test initial values"""
		self.assertEqual(self.e.amount, 1)
		self.assertEqual(self.e.name, 'base_item')
		
	def test_drink_method(self):
		"""Drink method should decraese items amount by 1 and produce message"""
		msg = self.e.drink(self.h)
		self.assertEqual(msg, self.h.name + ' drinks elixir, but nothing happens...')
		self.assertEqual(self.e.amount, 0)
	
	def test_drink_method_with_no_elixirs(self):
		"""Drink method should only display error message and not use the item"""
		self.e.amount = 0
		msg = self.e.drink(self.h)
		self.assertEqual(msg, self.h.name + ' has no '+self.e.name+"s left")
		self.assertEqual(self.e.amount, 0)


class TestHealingPotionClass(unittest.TestCase):
	"""Tests for HealingPotion class"""
	
	def setUp(self):
		self.e1 = HealingPotion()
		self.e0 = HealingPotion(amount = 0)
		self.h = Hero()
		self.h.max_hp = 30
		
	def test_basic_setup(self):
		"""Test initial values"""
		self.assertEqual(self.e1.amount, 1)
		self.assertEqual(self.e1.name, 'Healing potion')
		self.assertEqual(self.e0.amount, 0)
		
	def test_drink_method_hero_fullHP(self):
		"""Hero with full hp should not be able to use this elixir"""
		self.h.hp = self.h.max_hp
		msg = self.e1.drink(self.h)
		self.assertEqual(msg, self.h.name + ' has full HP!')
		self.assertEqual(self.e1.amount, 1)
		
	def test_drink_method_hero_lightly_wounded(self):
		"""Hero's hp should be increased, but not exceed max_hp"""
		light_wound = self.e1.healing - 2
		self.h.hp = self.h.max_hp - light_wound
		msg = self.e1.drink(self.h)
		self.assertEqual(msg, self.h.name + ': ' + str(light_wound) + ' HP restored.')
		self.assertEqual(self.e1.amount, 0)
		self.assertEqual(self.h.hp, self.h.max_hp)
	
	def test_drink_method_hero_heavily_wounded(self):
		"""Hero's hp should be increased, but not fully """
		heavy_wound = self.e1.healing + 2
		self.h.hp = self.h.max_hp - heavy_wound
		msg = self.e1.drink(self.h)
		self.assertEqual(msg, self.h.name + ': ' + str(self.e1.healing) + ' HP restored.')
		self.assertEqual(self.e1.amount, 0)
		self.assertEqual(self.h.hp, self.h.max_hp - heavy_wound + self.e1.healing)
		
	def test_drink_method_hero_dead(self):
		"""When dead, hero should not be resurrected with this item"""
		self.h.hp = 0
		msg = self.e1.drink(self.h)
		self.assertEqual(msg, self.h.name + ' cannot be resurrected with this item')
		self.assertEqual(self.e1.amount, 1)
		self.assertEqual(self.h.hp, 0)
	
	def test_drink_method_with_no_elixirs(self):
		"""Drink method should only display error message and not use the item"""
		self.e0.amount = 0
		msg = self.e0.drink(self.h)
		self.assertEqual(msg, self.h.name + ' has no '+self.e0.name+"s left")
		self.assertEqual(self.e0.amount, 0)
		
		
class TestManaPotionClass(unittest.TestCase):
	"""Tests for ManaPotion class"""
	def setUp(self):
		self.e1 = ManaPotion()
		self.e0 = ManaPotion(amount = 0)
		self.h = Hero()
		self.h.max_mana = 5
		
	def test_basic_setup(self):
		"""Test initial values"""
		self.assertEqual(self.e1.amount, 1)
		self.assertEqual(self.e1.name, 'Mana potion')
		self.assertEqual(self.e0.amount, 0)
		
	def test_drink_method_hero_full_mana(self):
		"""Hero with full hp should not be able to use this elixir"""
		self.h.mana = self.h.max_mana
		msg = self.e1.drink(self.h)
		self.assertEqual(msg, self.h.name + ' has full mana!')
		self.assertEqual(self.e1.amount, 1)
		
	def test_drink_method_hero_lightly_loss(self):
		"""Hero's hp should be increased, but not exceed max_mana"""
		light_loss = self.e1.mana_restore - 2
		self.h.mana = self.h.max_mana - light_loss
		msg = self.e1.drink(self.h)
		self.assertEqual(msg, self.h.name + ': ' + str(light_loss) + ' mana points restored.')
		self.assertEqual(self.e1.amount, 0)
		self.assertEqual(self.h.mana, self.h.max_mana)
		
	def test_drink_method_hero_heavily_loss(self):
		"""Hero's hp should be increased, but not fully """
		heavy_loss = self.e1.mana_restore + 2
		self.h.mana = self.h.max_mana - heavy_loss
		msg = self.e1.drink(self.h)
		self.assertEqual(msg, self.h.name + ': ' + str(self.e1.mana_restore) + ' mana points restored.')
		self.assertEqual(self.e1.amount, 0)
		self.assertEqual(self.h.mana, self.h.max_mana - heavy_loss + self.e1.mana_restore)
		
	def test_drink_method_with_no_elixirs(self):
		"""Drink method should only display error message and not use the item"""
		self.h.mana = self.h.max_mana - 1
		self.e0.amount = 0
		msg = self.e0.drink(self.h)
		self.assertEqual(msg, self.h.name + ' has no '+self.e0.name+"s left")
		self.assertEqual(self.e0.amount, 0)
	
if __name__ == '__main__':
	unittest.main()
