"""Implements elixir class and all objects connected with drinkable beverages"""
from .item import Item


class Elixir(Item):
	"""Base class for all elixirs"""
	def __init__(self):
		super().__init__()
		self.amount = 1
		
	def __repr__(self):
		return self.name + ' (' + repr(self.amount) + ')'
		
	def drink(self, hero):
		"""Consumes elixir"""
		if self.amount > 0:
			self.amount -= 1
			return '{} drinks elixir, but nothing happens...'.format(hero.name)
		else:
			return '{} has no {}s left'.format(hero.name, self.name)

	def serialize(self):
		data_out = super().serialize()
		data_out['class'] = self.__class__
		data_out['amount'] = self.amount
		return data_out


class HealingPotion(Elixir):
	"""Elixir that restores 10 HP"""
	def __init__(self, amount=1):
		super().__init__()
		self.name = 'Healing potion'
		self.description = 'Red colour, ugly taste, but damn you feel a lot better after drinking it'
		self.value = 10
		self.healing = 10
		self.amount = amount
	
	def drink(self, hero):
		"""Consumes elixir and heals 10 hp"""
		if hero.hp == hero.max_hp:
			return '{} has full HP!'.format(hero.name)
		elif hero.hp <= 0:
			return '{} cannot be resurrected with this item'.format(hero.name)
		elif self.amount > 0:
			curr_hp = hero.hp
			hero.set_hp(self.healing)
			healed_hp = hero.hp
			self.amount -= 1
			return '{}: {} HP restored.'.format(hero.name, str(healed_hp - curr_hp))
		else:
			return '{} has no {}s left'.format(hero.name, self.name)

	def serialize(self):
		data_out = super().serialize()
		data_out['healing'] = self.healing
		return data_out

class ManaPotion(Elixir):
	"""Elixir that restores 3 mana"""
	def __init__(self, amount=1):
		super().__init__()
		self.name = 'Mana potion' 
		self.description = 'After drinking this, you feel like doing special things'
		self.value = 5
		self.mana_restore = 3
		self.amount = amount
	
	def drink(self, hero):
		"""Consumes elixir and restores 3 mana"""
		if hero.mana == hero.max_mana:
			return '{} has full mana!'.format(hero.name)
		elif self.amount > 0:
			curr_mana = hero.mana
			hero.set_mana(self.mana_restore)
			restored_mana = hero.mana
			self.amount -= 1
			return '{}: {} mana points restored.'.format(hero.name, str(restored_mana - curr_mana))
		else:
			return '{} has no {}s left'.format(hero.name, self.name)

	def serialize(self):
		data_out = super().serialize()
		data_out['mana_restore'] = self.mana_restore
		return data_out


class SpeedElixir(Elixir):
	"""Potion that temporarily boosts speed"""
	pass
