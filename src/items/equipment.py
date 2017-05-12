from .weapons.weapon import *
from .shields.shield import WoodenShield
from .armors.armor import LeatherArmor


class Equipment():
	"""Base class for storing currently equiped stuff"""
	def __init__(self, weapon = Fist()):
		self.weapon = {'primary':weapon, 'special':weapon}
		self.shield = WoodenShield
		self.armor = LeatherArmor

		
		
