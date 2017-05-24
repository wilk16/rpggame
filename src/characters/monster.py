from .character import Character
from ..items.weapon import Fist, DragonClaw, ShortSword
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
	def __init__(self):
		super().__init__()
		self.name = 'Vampire'
		self.max_hp = 20
		self.hp = 20
		self.attack = 9
		self.defence = 9
		self.speed = 5
		self.exp = 2500
		self.level = 3
		self.inventory = []
		self.equipment = Equipment(weapon = VampireFangs())
	
class Ghul(Undead):
	"""Quasimodo, but dead. Undead"""
	pass
	
class Zombie(Undead):
	""" Braaaain guys"""
	def __init__(self):
		super().__init__()
		self.name = 'Zombie'
		self.max_hp = 10
		self.hp = 10
		self.attack = 1
		self.defence = 3
		self.speed = 1
		self.exp = 300
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
		self.max_hp = 20
		self.hp = 20
		self.attack = 7
		self.defence = 5
		self.speed = 6
		self.exp = 4000
		self.level = 5
		self.inventory = []
		self.equipment = Equipment(weapon = DragonClaw())

class Skeleton(Undead):
	"""Lowest form of undead. Bones and arrows"""
	def __init__(self):
		super().__init__()
		self.name = 'Skeleton'
		self.max_hp = 5
		self.hp = 5
		self.attack = 3
		self.defence = 2 # attack + 1k20 >= defence
		self.speed = 3
		self.exp = 100
		self.level = 1
		self.inventory = []
		self.equipment = Equipment(weapon = ShortSword())
	
MONSTER_COLLECTION = {1: [Skeleton,],
	2:[Zombie,],
	3:[DragonHatchling,],
	4:[],
	5:[SkeletalDragon,]}
