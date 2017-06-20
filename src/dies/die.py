"""Little things that make many rpg games possible"""
from random import randint


class Die:
	"""Base class for dies"""
	def __init__(self, amount, sides):
		self.sides = sides
		self.amount = amount
		
	def roll(self):
		"""Simulate a dice roll. If a die has amount more than 1, then
		results from rolls are summed."""
		rolls = [randint(1, self.sides) for _ in range(0, self.amount)]
		return sum(rolls)
		
	def __repr__(self):
		return str(self.amount)+'k'+str(self.sides)
		
	def __eq__(self, obj):
		return True if (self.amount == obj.amount) & (self.sides == obj.sides) else False

	def serialize(self):
		return {'sides': self.sides, 'amount': self.amount}