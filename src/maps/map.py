"""Map implements classes for levels and Tiles of which levels are made
The hero travels down next levels and on each of them explores different Tiles"""

from itertools import product
from ..characters.monster import MONSTER_COLLECTION
from random import choice, randint
from ..characters.hero import Hero
from ..misc.const import DIRECTIONS, MAP_TILE_X, MAP_TILE_Y
from ..misc.misc import clear_display, msg_log

class Level:
	
	def __init__(self, depth = 1):
		self.dim = 5
		self.depth = depth
		self.artifact = None
		self.hero = None
		self.tiles = [[Tile() for j in range(0, self.dim)] for i in range(0, self.dim)]
		self.boss_beaten = False

	def generate_random_level(self):
		""""Generates level with randomly placed MonsterTiles, HealthTiles, etc."""
		
		# Dictionary with specific tiles amount per level
		tile_dict = {'monster': (MonsterTile, 5),
					'healing': (HealthTile, 2),
					'boss': (BossTile, 1),
					'mana': (ManaTile, 1),}
					

		empty_tiles = [(x, y) for x in range(0, self.dim) for y in range(0, self.dim) if (x, y)!=(2, 2)]
		
		# SpawnTile should always be in the middle
		self.tiles[int(self.dim/2)][int(self.dim/2)] = SpawnTile()
		
		for key in tile_dict:
			for i in range(0, tile_dict[key][1]):
				x, y = choice(empty_tiles)
				del empty_tiles[empty_tiles.index((x,y))]
				self.tiles[x][y] = tile_dict[key][0](level = self.depth)


	def generate_sample_level(self):
		# generate the same level for testing purposes
		self.tiles = [[MonsterTile(level = self.depth), Tile(), Tile(),Tile(), Tile()],
					[Tile(),Tile(), Tile(), Tile(),Tile()],
					[Tile(), MonsterTile(level = self.depth), SpawnTile(), HealthTile(), Tile()],
					[Tile(), Tile(), Tile(),MonsterTile(level = self.depth),Tile()],
					[Tile(), BossTile(), Tile(),Tile(), Tile()]]
					
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
		""" Actions when hero steps on a tile. Make tile visited, surrounding 
		visible and perform tiles action """
		
		# perform action connected to tile
		if self.tiles[x][y].visited == 0:
			self.tiles[x][y].action(hero = self.hero, enemy = self.tiles[x][y].enemy)
			
		# if this is a BossTile & and hero killed the boss then go level deeper
		if isinstance(self.tiles[x][y], BossTile) & self.hero.isAlive():
			_=clear_display()
			print(msg_log.display_log())
			self.boss_beaten = True
		
			
		# explore new and surrounding tiles
		self.tiles[x][y].visited = 1
		
		if (x-1 >= 0) & (x-1 < self.dim):
			self.tiles[x-1][y].visible = 1
		if (x+1 >= 0) & (x+1 < self.dim):
			self.tiles[x+1][y].visible = 1
		if (y+1 >= 0) & (y+1 < self.dim):
			self.tiles[x][y+1].visible = 1
		if (y-1 >= 0) & (y-1 < self.dim):
			self.tiles[x][y-1].visible = 1

		
		
	def enter_hero(self, hero):
		"""Prepare level for hero entrance"""
		self.hero = hero
		self.max_depth_reached = self.depth
		middle = int(self.dim/2)
		self.hero.xy = [middle, middle]
		self.visit_tile(self.hero.xy[0], self.hero.xy[1])
		self.tiles[self.hero.xy[0]][self.hero.xy[1]].symbol = 'H'
		
	def move_hero(self, hero):
		"""Main loop while exploring a level, moves hero around"""
		while self.boss_beaten == False:
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
				_=input('bad decision\n')
		
		
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
		Hero.battle(kwargs['hero'], kwargs['enemy'])
		
class BossTile(MonsterTile):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.enemy = choice(MONSTER_COLLECTION[kwargs['level']+2])()
		self.symbol = 'B'
		self.action = BossTile.battle
		
	def battle(**kwargs):
		Hero.battle(kwargs['hero'], kwargs['enemy'])
		if kwargs['hero'].isAlive():
			msg_log.insert("You've beaten the boss of this level.\nBehind him you see another stairs leading down...")
	
class RestorationTile(Tile):
	def __init__(self, **kwargs):
		super().__init__()
	
	
class ManaTile(RestorationTile):
	"""Special tile that replenishes mana"""
	def __init__(self, **kwargs):
		super().__init__()
		self.symbol = 'm'
		self.action = ManaTile.restore_mana
		
	def restore_mana(**kwargs):
		"""Restores heroe's full mana"""
		msg_log.insert(kwargs['hero'].name +"'s full mana was restored.")
		kwargs['hero'].mana = kwargs['hero'].max_mana
	
class HealthTile(RestorationTile):
	"""Special tile that replenishes health"""
	def __init__(self, **kwargs):
		super().__init__()
		self.symbol = '+'
		self.action = HealthTile.restore_health
		
	def restore_health(**kwargs):
		"""Restores heroe's full health"""
		msg_log.insert(kwargs['hero'].name +"'s full health was restored.")
		kwargs['hero'].hp = kwargs['hero'].max_hp
	
	
	
