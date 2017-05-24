#initialize
from .characters.hero import Fighter, Paladin, Hero
from .characters.monster import Zombie, DragonHatchling, SkeletalDragon
from .items.weapon import *
from .dies.die import Die
from .misc.misc import EventLog
from .maps.map import *

f = Fighter()
p = Paladin()
z = Zombie()
d = DragonHatchling()
s = SkeletalDragon()

h = f

depth = 1
while 1==1:
	h.hp = h.max_hp
	h.mana = h.max_mana
	l = Level(depth = depth)
	l.generate_random_level()
	l.enter_hero(f)
	l.move_hero(f)
	del l
	if f.isAlive():
		depth += 1
	else:
		print('Game over sucker')
		break

