"""A set of additional functions used across the whole project"""
from .const import *
import os
import platform
import sys

def printLine(txt):
	#helper function for printing pretty lines
	return ('-- '+txt + (ROW_LEN-len(txt)-6)*' ' + ' --\n')

if platform.system() == 'Windows':
	clear_display = lambda: os.system('cls')
	os.system('mode con: cols=80 lines=40')
else:
	clear_display = lambda: os.system('clear')
	sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=80))

class EventLog():
	"""Class for storing a displaying messages collected during battles"""
	def __init__(self):
		"""Initialize with empty message list and message count = 0"""
		self.message = []
		self.length = 0
			
	def __repr__(self):
		return(str(self.length))
		
	def display_log(self):
		"""Display 10 lines with most recently logged messages. 
		
		If there are fewer lines, then leave unused lines blank, by still
		format to 10 rows"""
		msg = ''
		for i in range(1,11):
			if len(self.message) - 11 + i >= 0:
				msg+=('* ' + self.message[len(self.message) - 11 +i]+'\n')
			else:
				msg+=('* '+'\n')
		#print(msg)
		return(msg)
		 
	def insert(self, msg):
		if len(msg.split('\n')) > 1:
			for line in msg.split('\n'):
				self.message.append(line)
				self.length += 1
		else:
			self.message.append(msg)
			self.length += 1
msg_log = EventLog()
