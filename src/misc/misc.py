"""A set of additional functions used across the whole project"""
from .const import *
from os import system

def printLine(txt):
	#helper function for printing pretty lines
	return ('-- '+txt + (ROW_LEN-len(txt)-6)*' ' + ' --\n')

def clear_display():
	_=system('clear')

class EventLog():
	def __init__(self):
		self.message = []
		self.length = 0
			
	def __repr__(self):
		return(str(self.length))
		
	def display_log(self):
		msg = ''
		for i in range(1,11):
			if len(self.message) - 11 + i >= 0:
				msg+=('* ' + self.message[len(self.message) - 11 +i]+'\n')
			else:
				msg+=('* '+'\n')
				
		print(msg)
		 
	def insert(self, msg):
		if len(msg.split('\n')) > 1:
			for line in msg.split('\n'):
				self.message.append(line)
				self.length += 1
		else:
			self.message.append(msg)
			self.length += 1
