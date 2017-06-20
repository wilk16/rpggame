class Item:
	"""Base class for different items"""
	def __init__(self, name='base_item', description='base_description', value=0):
		self.name = name
		self.description = description
		self.value = value

	def __repr__(self):
		return self.name

	def serialize(self):
		return {'class': self.__class__, 'name': self.name, 'description': self.description, 'value': self.value}



