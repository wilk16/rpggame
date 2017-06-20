from .item import Item


class Shield(Item):
	"""Base class for shields"""
	def __init__(self):
		super().__init__()
		self.defence = 0

	def serialize(self):
		data_out = super().serialize()
		# data_out['class'] = self.__class__
		data_out['defence'] = self.defence
		return data_out


class WoodenShield(Shield):
	"""Simple round, wooden shield"""
	def __init__(self):
		super().__init__()
		self.defence = 3
		self.value = 10
		self.name = 'Wooden shield'
		self.description = 'A round shield made from a fine oak tree'
