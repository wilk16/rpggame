from .weapon import *
from .shield import WoodenShield
from .armor import LeatherArmor

from ..misc.misc import printLine
from ..misc.const import ROW_LEN

class Equipment():
	"""Base class for storing currently equiped stuff"""
	def __init__(self, weapon = Fist(), elixir = []):
		self.weapon = weapon
		self.shield = WoodenShield
		self.armor = LeatherArmor
		self.elixir = elixir
