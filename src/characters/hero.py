from .character import Character
from .level_mat import lvl
from ..items.weapon import ShortSword
from ..items.equipment import Equipment
from ..items.elixir import HealingPotion, ManaPotion
from ..dies.die import Die
from .monster import Undead
from ..misc.misc import msg_log, clear_display
from ..misc.const import ADD, MUL


class Hero(Character):
	"""Base class for players profession"""
	def __init__(self):
		super().__init__()
		self.attribute.append('Human')
		self.equipment = Equipment(elixir=[HealingPotion(2), ManaPotion(3)], weapon=ShortSword())
		self.actions = {'a': self.attack_enemy}
		self.xy = [None, None]
		self.max_depth_reached = 1

	def level_up(self):
		"""Raise hero's level"""
		self.level += 1
		self.max_hp += 15
		self.hp += 15
		self.max_mana += 1
		self.mana += 1
		return "Level Up!"

	def set_exp(self, val):
		"""Add/remove hero's exp"""
		msg = ''
		self.exp += val
		msg += (self.name + ' gained ' + str(val) + ' exp.\n')
		if lvl[self.level] <= self.exp:
			msg += self.level_up()
		return msg.strip()

	def serialize(self):
		data_out = {'class': self.__class__, 'max_hp': self.max_hp, 'attack': self.attack,
					'profession': self.profession, 'max_mana': self.max_mana, 'defence': self.defence,
					'level': self.level, 'speed': self.speed, 'max_depth_reached': self.max_depth_reached,
					'exp': self.exp, 'name': self.name, 'attribute': self.attribute,
					'equipment': self.equipment.serialize()}
		return data_out

	def battle(self, enemy):
		"""implements fighting against an enemy"""
		# msg_log = EventLog()
		msg_log.insert('You enter a battle with {}'.format(enemy.name))
		
		while 1 == 1:
			
			clear_display()
			print(msg_log.display_log())
				
			self.view_battle_stats(enemy)
			action = input("""\nPress a for attack and s for special move,\nb for boost and e to use an elixir:\n""")
			if action not in ('a', 's', 'b', 'e'):
				continue
			elif action == 'e':
				print()
				for i in range(1, len(self.equipment.elixir)+1):
					print(str(i)+') ' + self.equipment.elixir[i-1].name + ' [' + str(self.equipment.elixir[i-1].amount) + ']')
				elixir_action = input('Type number of elixir to drink:\n')
			if self.speed >= enemy.speed:
				if action == 'e':
					msg_log.insert(self.equipment.elixir[int(elixir_action)-1].drink(self))
				else:
					msg_log.insert(self.actions[action](enemy))
					if not enemy.is_alive():
						msg_log.insert(self.name + ' killed ' + enemy.name)
						msg_log.insert(self.set_exp(enemy.exp))
						msg_log.insert('Press any key...')
						clear_display()
						print(msg_log.display_log())
						self.view_battle_stats(enemy)
						_=input('')
						break
				msg_log.insert(enemy.attack_enemy(self))
				if not self.is_alive():
					print(enemy.name + ' killed ' + self.name)
					clear_display()
					print(msg_log.display_log())
					self.view_battle_stats(enemy)
					_=input('')
					break
			else:
				msg_log.insert(enemy.attack_enemy(self))
				if not self.is_alive():
					msg_log.insert(enemy.name + ' killed ' + self.name)
					clear_display()
					print(msg_log.display_log())
					self.view_battle_stats(enemy)
					_=input('')
					break
				if action == 'e':
					msg_log.insert(self.equipment.elixir[elixir_action].drink(self))
				else:
					msg_log.insert(self.actions[action](enemy))
					if not enemy.is_alive():
						msg_log.insert(self.name + ' killed ' + enemy.name)
						msg_log.insert(self.set_exp(enemy.exp))
						clear_display()
						print(msg_log.display_log())
						self.view_battle_stats(enemy)
						_ = input('')
						break
				

class Fighter(Hero):
	""""Fighter class, attack """
	def __init__(self, name='fighty'):
		super().__init__()
		self.name = name
		self.profession = 'Fighter'
		self.attack = 3
		self.defence = 12
		self.actions['s'] = self.charge 
		self.actions['b'] = self.bulk_up
			
	def bulk_up(self, enemy):
		"""Raise fighters attack"""
		self.attack += 1
		return self.name + "'s attack rose +1"
		
	def charge(self, enemy):
		"""Attack with 3x rolls"""
		msg = ''
		# check if hero has enough mana
		if self.mana <= 0:
			msg += self.name + ": out of mana. Use normal attack\n"
			# attack
			msg += self.attack_enemy(enemy)
		else:
			primary_die = self.equipment.weapon.die
			
			# boost weapon's die
			change_weapon = {'side_op': ADD, 'side_val': 0, 'amount_op': MUL, 'amount_val': 3}
			self.equipment.weapon.modify_weapon_die(**change_weapon)
			
			# attack
			msg += self.name + ' charged!\n'
			msg += self.attack_enemy(enemy)
			
			# reduce mana
			self.set_mana(-1)
			
			# restore state
			self.equipment.weapon.restore_weapon_die(die=primary_die)
		return msg


class Paladin(Hero):
	"""Paladin class, special powers for fighting with undead"""
	def __init__(self, name='holymoly'):
		super().__init__()
		self.name = name
		self.profession = 'Paladin'
		self.attack = 2
		self.defence = 13
		self.actions['s'] = self.holy_strike 
		self.actions['b'] = self.block
			
	def block(self, enemy):
		"""Raise paladins defence"""
		self.defence += 1
		print(self.name + "''s attack rose +1")
	
	def holy_strike(self, enemy):
		"""Attack with divine help by adding +4 to attack die. If the enemy is undead
		add secod throw."""
		msg = ''
		# check if hero has enough mana
		if self.mana <= 0:
			msg += self.name + ": out of mana. Use normal attack\n"
			# attack
			msg += self.attack_enemy(enemy)
		else:
			# boost weapon's die
			primary_die = self.equipment.weapon.die
			if isinstance(enemy, Undead):
				self.equipment.weapon.die = Die(primary_die.amount*2, primary_die.sides+4)
			else:
				self.equipment.weapon.die = Die(primary_die.amount, primary_die.sides+4)
			msg += self.name + ' used holy strike!\n'
			
			# attack
			msg += self.attack_enemy(enemy)
			
			# reduce mana
			self.set_mana(-1)
			
			# restore weapon's state
			self.equipment.weapon.die = Die(primary_die.amount, primary_die.sides)
		return msg
