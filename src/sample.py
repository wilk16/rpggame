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


def game_loop():
	h = f
	depth = 1
	
	while 1==1:
		h.hp = h.max_hp
		h.mana = h.max_mana
		if depth == h.max_depth_reached:
			# hero must have previously died, so he will start 2 levels before
			l = Level(depth = max(1, h.max_depth_reached-2))
		else:
			l = Level(depth = depth)
			
		l.generate_random_level()
		l.enter_hero(f)
		l.move_hero(f)
		del l
		if f.isAlive():
			depth += 1
		else:
			print('Game over sucker!')
	
	
game_loop()
	
