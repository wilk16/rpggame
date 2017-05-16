from .item import Item
from ..dies.die import Die
		
class Shield(Item):
	"""Base class for shields"""
	def __init__(self):
		super().__init__()
		self.item_type = 'shield'

class WoodenShield(Shield):
	"""Simple round, wooden shield"""
	def __init__(self):
		super().__init__()
		self.defence = 3
		self.value = 10
		self.name = 'Wooden shield'
		self.description = 'A round shield made from a fine oak tree'
