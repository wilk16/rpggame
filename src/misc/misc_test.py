import unittest
from .misc import EventLog

class TestEventLogClass(unittest.TestCase):
	def setUp(self):
		self.e = EventLog()
		
	def test_basic_setup(self):
		assertIsEmpty(self.e.message)
		assertEqual(self.e.length, 0)


if __name__ == '__main__':
    unittest.main()
