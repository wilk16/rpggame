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
		if self.amount > 0:
			self.amount -=1
			return(hero.name + ' drinks elixir, but nothing happens...')
		else:
			return(hero.name + ' has no '+self.name+"s left")

class HealingPotion(Elixir):
	"""Elixir that restores 10 HP"""
	def __init__(self, amount=1):
		self.name = 'Healing potion'
		self.description = 'Red colour, ugly taste, but damn you feel a lot better after drinking it'
		self.value = 10
		self.healing = 10
		self.amount = amount
	
	def drink(self, hero):
		if hero.hp == hero.max_hp:
			return(hero.name + ' has full HP!')
		elif self.amount > 0:
			curr_hp = hero.hp
			hero.set_hp(self.healing)
			healed_hp = hero.hp
			self.amount -=1
			return(hero.name + ': ' + str(healed_hp - curr_hp) + ' HP restored.')
		else:
			return(hero.name + ' has no '+self.name+"s left")
	
	
	
class SpeedElixir(Elixir):
	"""Potion that temporarily boosts speed"""
	pass
