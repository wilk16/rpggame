#initialize
from .characters.hero import Fighter, Paladin, Hero
from .characters.monster import Zombie, DragonHatchling, SkeletalDragon
from .items.weapon import *
from .dies.die import Die
from .misc.misc import EventLog

f = Fighter()
p = Paladin()
z = Zombie()
d = DragonHatchling()
s = SkeletalDragon()


e = EventLog()
msg_1 = 'aaa'
msg_2 = 'battle\nattack'
