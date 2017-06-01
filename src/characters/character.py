from ..items.equipment import Equipment
from ..dies.die import Die
from ..misc.misc import printLine
from ..misc.const import ROW_LEN

class Character:
	
	def __init__(self, name = 'some_name', max_hp=15, attack=0,\
			defence=0, speed=5, exp=0, level = 1, max_mana = 5):
		self.hp = max_hp
		self.name =name
		self.max_hp = max_hp
		self.max_mana = max_mana
		self.mana = max_mana
		self.attack = attack
		self.defence = defence
		self.speed = speed
		self.level = level
		self.exp = exp
		self.inventory = []
		self.equipment = Equipment()
		self.dies = {'d1k20' : Die(1,20)}
		self.attribute = []

	def isAlive(self):
		"""Returns 1 if character is alive"""
		if self.hp <= 0:
			return 0
		else:
			return 1

	def set_hp(self, val):
		"""Change hp, positive val adds hp, negative substracts"""
		self.hp = max(min(self.hp + val, self.max_hp), 0)
		
		
	def set_mana(self, val):
		"""Change mana, positive val adds mana, negative substracts"""
		self.mana = max(min(self.mana + val, self.max_mana), 0)

	def show_stats(self):
		msg = ''
		msg += ROW_LEN*'-'+'\n'
		msg += printLine(str(self.name).upper() + ' STATISTICS: ')
		msg += ROW_LEN*'*'+'\n'
		msg += printLine('Level: ' + str(self.level))
		msg += printLine('Exp: ' + str(self.exp))
		msg += printLine('HP: ' + str(self.hp) + '/' + str(self.max_hp))
		msg += printLine('Mana: ' + str(self.mana) + '/' + str(self.max_mana))
		msg += printLine('Attack: ' + str(self.attack))
		msg += printLine('Defence: ' + str(self.defence))
		msg += printLine('Speed: ' + str(self.speed))
		msg += ROW_LEN*'-'+'\n'
		print(msg)

	def show_equipment(self):
		msg = ''
		msg += ROW_LEN*'-'+'\n'
		msg += printLine(str(self.name).upper() + ' EQUIPMENT: ')
		msg += ROW_LEN*'*'+'\n'
		msg += printLine('Weapon: ' + str(self.equipment.weapon))
		msg += ROW_LEN*'-'+'\n'
		print(msg)
		
	def get_mana(self):
		"""Function that returns mana status in a battle-friendly format"""
		return('*'*(self.max_mana-self.mana) + 'o'*self.mana)
		 
	def view_battle_stats(self, enemy):
		msg = ''
		msg += ROW_LEN*'-'+'\n'
		msg += printLine((str(enemy.name).upper() + '(' + str(enemy.level) + ') ' + enemy.get_mana()).ljust(ROW_LEN-6, ' '))
		msg += printLine(('HP: ' + str(enemy.hp) + '/' + str(enemy.max_hp)).ljust(ROW_LEN-6, ' '))
		msg += ROW_LEN*'-'+'\n'
		msg += printLine('VS'.center(ROW_LEN-6, ' '))
		msg += ROW_LEN*'-'+'\n'
		msg += printLine((self.get_mana() + ' '+ str(self.name).upper() + '(' + str(self.level) + ')').rjust(ROW_LEN-6, ' '))
		msg += printLine(('HP: ' + str(self.hp) + '/' + str(self.max_hp)).rjust(ROW_LEN-6, ' '))
		msg += ROW_LEN*'-'+'\n'
		print(msg)
		 
		 
	def attack_enemy(self, enemy):
		msg = ''
		attack_throw = self.dies['d1k20'].roll()
		if attack_throw + self.attack > enemy.defence:
			if attack_throw >= 18:
				msg+=("""{0}: Attack throw {1} - critical hit!\n""".\
				format(self.name, attack_throw))
				primary_die = self.equipment.weapon.die
				self.equipment.weapon.die = Die(primary_die.amount*2, primary_die.sides)
				damage = self.equipment.weapon.die.roll()
				#restore state
				self.equipment.weapon.die = Die(primary_die.amount, primary_die.sides)
			else:
				msg+=("""{0}: Attack throw {1} - hit!\n""".\
					format(self.name, attack_throw))
				damage = self.equipment.weapon.die.roll()

			enemy.set_hp(-damage)
			if damage > 0:
				msg+=("""{0}: hit {1} for {2}""".\
					format(self.name, enemy.name, damage))
		else:
			msg+=("""{0}: Attack throw {1} - miss!""".\
				format(self.name, attack_throw))
		return(msg)
