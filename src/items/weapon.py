"""Implements weapon class and all objects connected with weapons and dealing damage"""

from .item import Item
from ..dies.die import Die

class Weapon(Item):
	"""Base class for all weapons"""
	def __init__(self):
		super().__init__()
		self.die = Die(1,1)
		
	def __repr__(self):
		return self.name + ' (' + repr(self.die) + ')'

class BluntWeapon(Weapon):
	"""Base class for blunt weapons"""
	def __init__(self):
		super().__init__()

class SlashWeapon(Weapon):
	"""Base class for slash weapons"""
	def __init__(self):
		super().__init__()
class RangeWeapon(Weapon):
	"""..."""
	def __init__(self):
		super().__init__()
class DrivenWeapon(Weapon):
	"""..."""
	def __init__(self):
		super().__init__()
		

class DragonClaw(SlashWeapon):
	"""Dragon's main weapon"""
	def __init__(self):
		super().__init__()
		self.die = Die(2,4)
		self.value = 0
		self.name = 'Dragon claws'
		self.description = 'Deadly sharp and feared magical claws'

class Fist(BluntWeapon):
	"""Most basic weapon of all human-like creatures"""
	def __init__(self):
		super().__init__()
		self.die = Die(1,2)
		self.value = 0
		self.name = 'Fists'
		self.description = 'Your bare fists - no more, no less'
		
class ShortSword(SlashWeapon):
	"""Cheapest, yet sharp sword"""
	def __init__(self):
		super().__init__()
		self.die = Die(1,4)
		self.value = 15
		self.name = 'Short sword'
		self.description = 'A typical short sword with iron blade.'

class Ashbringer(SlashWeapon):
	"""Meaningful comment"""
	def __init__(self):
		super().__init__()
		self.die = Die(2,7)
		self.value = 100
		self.name = 'Ashbringer'
		self.description = 'Very good blade to promote the light.'
		
class WoodenBow(RangeWeapon):
	"""Meaningful comment"""
	def __init__(self):
		super().__init__()
		self.die = Die(2,5)
		self.value = 5
		self.name = 'WoodenBow'
		self.description = 'Not bad Range Weapon.'
		
class DwarfHammer(BluntWeapon):
	"""Meaningful comment"""
	def __init__(self):
		super().__init__()
		self.die = Die(3,10)
		self.value = 75
		self.name = 'DwarfHammer'
		self.description = 'Epic, ancient Hammer!!!.'		
		
class Axe(SlashWeapon):
	"""Meaningful comment"""
	def __init__(self):
		super().__init__()
		self.die = Die(1,3)
		self.value = 20
		self.name = 'Axe'
		self.description = 'An tipical axe.'
		
class VampireFangs(DrivenWeapon):
	"""A Vamire's main weapon"""
	def __init__(self):
		super().__init__()
		self.die = Die(3,10)
		self.value = 0
		self.name = 'VampireFangs'
		self.description = 'Deadly and bloody fangs.'			
				
class WolfFangs(DrivenWeapon):
	"""A Wolf's main weapon"""
	def _init_(self):
		super()._init_()
		self.die = Die(2,3)
		self.value = 0
		self.name = 'WalfFangs'
		self.description = 'Dangerous and hungry fangs.'


