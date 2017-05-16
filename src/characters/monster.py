from .character import Character
from ..items.weapon import Fist, DragonClaw
from ..items.equipment import Equipment

class Monster(Character):
	"""Base class for all foes"""
	def __init__(self):
		super().__init__()

class Spider(Monster):
	"""Base class for all spider-like creatures"""
	def __init__(self):
		super().__init__()
		self.attribute.append('Spider')
	
class Wolf(Monster):
	"""Base class for different species of wolves"""
	def __init__(self):
		super().__init__()
		self.attribute.append('Beast')

class Dragon(Monster):
	"""Base class for different mighty dragons"""
	def __init__(self):
		super().__init__()
		self.attribute.append('Dragon')

class Undead(Monster):
	"""Base class for undead monsters"""
	def __init__(self):
		super().__init__()
		self.attribute.append('Undead')
		
class Vampire(Undead):
	"""Dracula, Regis, Edward and other shiny fellows"""
	pass
	
class Ghul(Undead):
	"""Quasimodo, but dead. Undead"""
	pass
	
class Zombie(Undead):
	""" Braaaain guys"""
	def __init__(self):
		super().__init__()
		self.name = 'Zombie'
		self.max_hp = 10
		self.attack = 1
		self.defence = 3
		self.speed = 1
		self.exp = 100
		self.level = 2
		self.inventory = []
		self.equipment = Equipment(weapon = Fist())

class DragonHatchling(Dragon):
	"""Young but still deadly dragon youngster"""
	def __init__(self):
		super().__init__()
		self.name = 'Dragon hatchling'
		self.max_hp = 30
		self.hp = 30
		self.attack = 7
		self.defence = 8
		self.speed = 7
		self.exp = 2000
		self.level = 3
		self.inventory = []
		self.equipment = Equipment(weapon = DragonClaw())
		
class SkeletalDragon(Dragon, Undead):
	"""Old dragon, combining dragonish and undeadish"""
	def __init__(self):
		super().__init__()
		self.name = 'Skeletal dragon'
		self.max_hp = 50
		self.hp = 50
		self.attack = 7
		self.defence = 5
		self.speed = 6
		self.exp = 4000
		self.level = 4
		self.inventory = []
		self.equipment = Equipment(weapon = DragonClaw())

class Skeleton(Undead):
	"""Lowest form of undead. Bones and arrows"""
	pass
	
