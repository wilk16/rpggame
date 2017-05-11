from ..items.weapons.weapon import Fist
from ..dies.die import Die


ROW_LEN = 40


def printLine(txt):
	#helper funciton for printing pretty lines
	return ('-- '+txt + (ROW_LEN-len(txt)-5)*' ' + '--\n')

class Character:
	
	def __init__(self, name = 'some_name', max_hp=10, attack=0,\
			defence=0, speed=5, exp=0, level = 1, equipment={'weapon':Fist()}):
		self.hp = max_hp
		self.name =name
		self.max_hp = max_hp
		self.attack = attack
		self.defence = defence
		self.speed = speed
		self.level = level
		self.exp = exp
		self.inventory = inventory
		self.equipment = equipment
		self.dies = {'d1k20' : Die(1,20)}
		self.attribute = []

	def isAlive(self):
		if self.hp <= 0:
			print(self.name + " is down!")
			return 0
		else:
			return 1

	def set_hp(self, val):
		self.hp = max(min(self.hp + val, self.max_hp), 0)


	def show_stats(self):
		msg = ''
		msg += ROW_LEN*'-'+'\n'
		msg += printLine(str(self.name).upper() + ' STATISTICS: ')
		msg += ROW_LEN*'*'+'\n'
		msg += printLine('Level: ' + str(self.level))
		msg += printLine('Exp: ' + str(self.exp))
		msg += printLine('HP: ' + str(self.hp) + '/' + str(self.max_hp))
		msg += printLine('Attack: ' + str(self.attack))
		msg += printLine('Defence: ' + str(self.defence))
		msg += printLine('Speed: ' + str(self.speed))
		msg += ROW_LEN*'-'+'\n'
		print(msg)
		
		
	def show_equipemnt(self):
		pass
		 
	def melee_attack(self, enemy):
		attack_throw = self.dies['d1k20'].roll()
		if attack_throw + self.attack > enemy.defence:
			print("""{0}: Attack throw {1} - hit!""".\
				format(self.name, attack_throw))
			damage = max(self.equipment['weapon'].die.roll(), 0)
			enemy.set_hp(-damage)
			if damage > 0:
				print("""{0}: hit {1} for {2}""".\
					format(self.name, enemy.name, damage))
		else:
			print("""{0}: Attack throw {1} - miss!""".\
				format(self.name, attack_throw))
