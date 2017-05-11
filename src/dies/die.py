from random import randint

class Die():
	def __init__(self, amount, sides):
		self.sides = sides
		self.amount = amount
		
	def roll(self):
		rolls = [randint(1,self.sides) for i in range(0,self.amount)]
		return sum(rolls)
		
	def __repr__(self):
		return str(self.amount)+'k'+str(self.sides)
		
