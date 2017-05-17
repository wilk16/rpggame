import unittest
from .die import Die


class TestDieClass(unittest.TestCase):
	"""Tests for Die class"""
	
	def setUp(self):
		self.d1k10 = Die(1,10)
		self.d2k4 = Die(2,4)
		
	def test_basic_setup(self):
		"""Test initial values"""
		self.assertEqual(self.d1k10.amount, 1)
		self.assertEqual(self.d1k10.sides, 10)
		self.assertEqual(self.d2k4.amount, 2)
		self.assertEqual(self.d2k4.sides, 4)
		
	def test_roll_method_min_max_single_die(self):
		"""Roll one die many times, and see if min and max values are in desired range"""
		rolls = [self.d1k10.roll() for i in range(1, 100)]
		self.assertGreaterEqual(self.d1k10.sides * self.d1k10.amount, min(rolls))
		self.assertLessEqual(self.d1k10.sides * self.d1k10.amount, max(rolls))
		
	def test_roll_method_min_max_double_die(self):
		"""Roll two dies many times, and see if min and max values are in desired range"""
		rolls = [self.d2k4.roll() for i in range(1, 100)]
		self.assertGreaterEqual(self.d2k4.sides * self.d2k4.amount, min(rolls))
		self.assertLessEqual(self.d2k4.sides * self.d2k4.amount, max(rolls))
