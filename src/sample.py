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

l = Level()
l.generate_random_level()
l.enter_hero(f)
l.move_hero(f)

