class Item:
	"""Base class for different items"""
	def __init__(self, name = 'base_item', description = 'base_description', value = 0, amount = 0):
		self.name = name
		self.description = description
		self.value = value

	def __repr__(self):
		return self.name



