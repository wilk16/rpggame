"""Implements weapon class and all objects connected with weapons and dealing damage"""

from .item import Item
from ..dies.die import Die

class Weapon(Item):
	"""Base class for all weapons"""
	def __init__(self):
		super().__init__()
		self.die = Die(1,1)
		
	def __repr__(self):
		return self.name + ' (' + repr(self.die) + ')'

class BluntWeapon(Weapon):
	"""Base class for blunt weapons"""
	def __init__(self):
		super().__init__()

class SlashWeapon(Weapon):
	"""Base class for slash weapons"""
	def __init__(self):
		super().__init__()
		

class DragonClaw(SlashWeapon):
	"""Dragon's main weapon"""
	def __init__(self):
		super().__init__()
		self.die = Die(2,8)
		self.value = 0
		self.name = 'Dragon claws'
		self.description = 'Deadly sharp and feared magical claws'

class Fist(BluntWeapon):
	"""Most basic weapon of all human-like creatures"""
	def __init__(self):
		super().__init__()
		self.die = Die(1,2)
		self.value = 0
		self.name = 'Fists'
		self.description = 'Your bare fists - no more, no less'
		
class ShortSword(SlashWeapon):
	"""Cheapest, yet sharp sword"""
	def __init__(self):
		super().__init__()
		self.die = Die(1,4)
		self.value = 15
		self.name = 'Short sword'
		self.description = 'A typical short sword with iron blade.'
