from .weapon import *
from .shield import WoodenShield


class Equipment:
	"""Base class for storing currently equipped stuff"""
	def __init__(self, weapon=Fist(), elixir=[]):
		self.weapon = weapon
		self.shield = WoodenShield()
		self.elixir = elixir

	def serialize(self):
		return {'class': self.__class__, 'weapon': self.weapon.serialize(), 'shield': self.shield.serialize(),
				'elixir': [elixir.serialize() for elixir in self.elixir]}
