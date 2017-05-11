from .character import Character
import level_mat as l_mat

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
		if l_mat.lvl[self.level] <=  self.exp:
			self.levelUp()
			
	def battle(self, enemy):
		"""implements fighting against an enemy"""
		
		print('You enter a battle with {}'.format(enemy.name))
		while 1==1:
			action = input('Press a for attack and s for special move\n')
			if action not in ('a', 's'):
				continue
			if self.speed >= enemy.speed:
				self.melee_attack(enemy)
				if not enemy.isAlive():
					print(self.name + ' killed ' + enemy.name)
					self.setExp(enemy.exp)
					break
				enemy.melee_attack(self)
				if not self.isAlive():
					print(enemy.name + ' killed ' + self.name)
					break
			else:
				enemy.melee_attack(self)
				if not self.isAlive():
					print(enemy.name + ' killed ' + self.name)
					break
				self.melee_attack(enemy)
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
			
	def bulk_up(self):
		"""Raise fighters attack"""
		self.attack+=1


class Paladin(Hero):
	"""Paladin class, special powers for fighting with undead"""
	def __init__(self, name = 'holymoly'):
		super().__init__()
		self.name = name
		self.profession = 'Paladin'
		self.attack = 2
		self.defence = 3
			
	def block(self):
		"""Raise paladins defence"""
		self.defence+=1
	
	def raise_spirit(self):
		"""Add a bonus to attack against undead"""
		pass
