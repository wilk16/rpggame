from .character import Character
from .level_mat import lvl
from ..items.weapons.weapon import ShortSword
from ..items.equipment import Equipment
from ..dies.die import Die

class Hero(Character):
	"""Base class for players profession"""
	def __init__(self):
		super().__init__()
		self.race = 'Human'
		
	def levelUp(self):
		"""Raise hero's level"""
		self.level += 1
		self.max_hp += 15
		print("Level Up!")

	def setExp(self, val):
		"""Add/remove hero's exp"""
		self.exp += val
		print(self.name +' gained ' + str(val) + ' exp.')
		if lvl[self.level] <=  self.exp:
			self.levelUp()
			
	def battle(self, enemy):
		"""implements fighting against an enemy"""
		
		print('You enter a battle with {}'.format(enemy.name))
		while 1==1:
			action = input('Press a for attack and s for special move\n')
			if action not in ('a', 's', 'b'):
				continue
			if self.speed >= enemy.speed:
				self.actions[action](enemy)
				if not enemy.isAlive():
					print(self.name + ' killed ' + enemy.name)
					self.setExp(enemy.exp)
					break
				enemy.attack_enemy(self)
				if not self.isAlive():
					print(enemy.name + ' killed ' + self.name)
					break
			else:
				enemy.attack_enemy(self)
				if not self.isAlive():
					print(enemy.name + ' killed ' + self.name)
					break
				self.actions[action](enemy)
				if not enemy.isAlive():
					print(self.name + ' killed ' + enemy.name)
					self.setExp(enemy.exp)
					break
				

class Fighter(Hero):
	""""Fighter class, attack """
	def __init__(self, name = 'fighty'):
		super().__init__()
		self.name = name
		self.profession = 'Fighter'
		self.attack = 3
		self.defence = 2
		self.equipment = Equipment(weapon = ShortSword())
		self.actions = {'a':self.attack_enemy,
						's':self.charge, 
						'b':self.bulk_up}
			
	def bulk_up(self, enemy):
		"""Raise fighters attack"""
		self.attack+=1
		print(self.name + "'s attack rose +1")
		
	def charge(self, enemy):
		"""Attack with 3x rolls"""
		
		#boost weapon's die
		primary_die = self.equipment.weapon['primary'].die
		self.equipment.weapon['special'].die = Die(primary_die.amount*3, primary_die.sides)
		#attack
		print(self.name + ' charged!')
		self.attack_enemy(enemy, 1)
		#restore state
		self.equipment.weapon['special'].die = Die(primary_die.amount, primary_die.sides)


class Paladin(Hero):
	"""Paladin class, special powers for fighting with undead"""
	def __init__(self, name = 'holymoly'):
		super().__init__()
		self.name = name
		self.profession = 'Paladin'
		self.attack = 2
		self.defence = 3
		self.equipment = Equipment(weapon = ShortSword())
		self.actions = {'a':self.attack_enemy,
						's':self.holy_strike, 
						'b':self.block}
			
	def block(self):
		"""Raise paladins defence"""
		self.defence+=1
		print(self.name + "''s attack rose +1")
	
	def holy_strike(self):
		"""Attack with divine help"""
		print(self.name + ' used holy strike!')
