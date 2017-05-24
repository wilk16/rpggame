from itertools import product
from ..characters.monster import MONSTER_COLLECTION
from random import choice
from ..characters.hero import Hero
from ..misc.const import DIRECTIONS, MAP_TILE_X, MAP_TILE_Y
from ..misc.misc import clear_display, msg_log

class Level:
	
	def __init__(self, dim = 5, depth = 1):
		self.dim = dim
		self.depth = depth
		self.boss = None
		self.artifact = None
		self.hero = None

		
	def generate_random_level(self):
		#will be random in the future
		self.tiles = [[MonsterTile(level = self.depth), Tile(), Tile(),Tile(), Tile()],
					[Tile(),Tile(), Tile(), Tile(),Tile()],
					[Tile(), MonsterTile(level = self.depth), SpawnTile(), HealthTile(), Tile()],
					[Tile(), Tile(), Tile(),MonsterTile(level = self.depth),Tile()],
					[Tile(), Tile(), Tile(),Tile(), Tile()]]
					
	def show_level(self):
		# prepare map for display
		level_diag = ''
		level_diag += ('LEVEL '+ str(self.depth)).center(self.dim*7+1, '=')+'\n\n'
		
		for i in range(0, self.dim):
			level_diag += self.dim * ('+' + '-'*MAP_TILE_X) + '+\n'
			level_diag += self.dim * ('|' + ' '*MAP_TILE_X) + '|\n'
			for j in range(0, self.dim):
				level_diag += '|' + ' '*int((MAP_TILE_X-3)/2) + (self.tiles[i][j].show_tile()).center(3, ' ') + ' '*int((MAP_TILE_X-3)/2)
			level_diag += '|\n'
			level_diag += self.dim * ('|' + ' '*MAP_TILE_X) + '|\n'
		level_diag += self.dim * ('+' + '-'*MAP_TILE_X) + '+\n'
		print(level_diag)
		
	def visit_tile(self, x, y):
		
		# perform action connected to tile
		if self.tiles[x][y].visited == 0:
			self.tiles[x][y].action(hero = self.hero, enemy = self.tiles[x][y].enemy)
			
		# explore new and surrounding tiles
		self.tiles[x][y].visited = 1
		
		try: 
			self.tiles[x-1][y].visible = 1
		except IndexError:
			pass
		try: 
			self.tiles[x+1][y].visible = 1
		except IndexError:
			pass
		try: 
			self.tiles[x][y+1].visible = 1
		except IndexError:
			pass
		try: 
			self.tiles[x][y-1].visible = 1
		except IndexError:
			pass
		
		
	def enter_hero(self, hero):
		self.hero = hero
		middle = int(self.dim/2)
		self.hero.xy = [middle, middle]
		self.visit_tile(self.hero.xy[0], self.hero.xy[1])
		self.tiles[self.hero.xy[0]][self.hero.xy[1]].symbol = 'H'
		
	def move_hero(self, hero):
		
		while 1 == 1:
			_=clear_display()
			print(msg_log.display_log())
			self.show_level()
			dir_dec = str.lower(input('\nWhere to go next?\n'))
			if dir_dec in DIRECTIONS:
				dx, dy = DIRECTIONS[dir_dec]
				
				if (self.hero.xy[0] + dx < 0) | (self.hero.xy[0] + dx >= self.dim):
					
					continue
				elif (self.hero.xy[1] + dy < 0) | (self.hero.xy[1] + dy >= self.dim):
					continue
				else:
					self.tiles[self.hero.xy[0]][self.hero.xy[1]].symbol = ' '
					self.hero.xy = [self.hero.xy[0] +dx, self.hero.xy[1] +dy]
					self.tiles[self.hero.xy[0]][self.hero.xy[1]].symbol = 'H'
					self.visit_tile(self.hero.xy[0], self.hero.xy[1])
			else:
				_=input('bad decision')
		
		
class Tile:
	
	def __init__(self):
		self.visited = 0
		self.visible = 0
		self.symbol = ''
		self.action = Tile.do_nothing
		self.enemy = None
		
	def show_tile(self):
		if self.symbol == 'H':
			return(self.symbol)
		elif self.visited == 1:
			return(' ')
		elif self.visible == 1:
			return(self.symbol)
		else: 
			return('?')
			
	def do_nothing(**kwargs):
		msg_log.insert('You enter an empty chamber...')

class SpawnTile(Tile):
	
	def __init__(self):
		super().__init__()
		self.symbol = 's'
		self.action = SpawnTile.enter_level
		
	def enter_level(**kwargs):
		msg_log.insert('You descend into another dark and gloomy dungeon level...')
	
class ShopTile(Tile):
	pass
	
class TreasureTile(Tile):
	pass
			
class MonsterTile(Tile):
	
	def __init__(self, **kwargs):
		super().__init__()
		self.enemy = choice(MONSTER_COLLECTION[kwargs['level']])()
		self.symbol = 'M'
		self.action = MonsterTile.battle
		
	def battle(**kwargs):
		msg_log.insert('You encounter a '+kwargs['enemy'].name)
		Hero.battle(kwargs['hero'], kwargs['enemy'])
		
class BossTile(MonsterTile):
	pass
	
class RestorationTile(Tile):
	def __init__(self, **kwargs):
		super().__init__()
	
	
class ManaTile(RestorationTile):
	pass
	
class HealthTile(RestorationTile):
	
	def __init__(self):
		super().__init__()
		self.symbol = '+'
		self.action = HealthTile.restore_health
		
	def restore_health(**kwargs):
		msg_log.insert(kwargs['hero'].name +"'s full health was restored.")
		kwargs['hero'].hp = kwargs['hero'].max_hp
	
	
	
