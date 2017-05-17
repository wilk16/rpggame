import unittest
from .misc import EventLog

class TestEventLogClass(unittest.TestCase):
	def setUp(self):
		self.e = EventLog()
		
	def test_basic_setup(self):
		self.assertEqual(self.e.message, [])
		self.assertEqual(self.e.length, 0)
		
	def test_insert_method_single_line_message(self):
		self.e.insert('One line message')
		self.assertEqual(self.e.length, 1)
		self.assertListEqual(self.e.message, ['One line message'])
		
	def test_insert_method_multiline_message(self):
		self.e.insert('Three\nline\nmessage')
		self.assertEqual(self.e.length, 3)
		self.assertListEqual(self.e.message, ['Three', 'line', 'message'])

	def test_display_log_with_no_messages(self):
		disp = self.e.display_log().strip()
		self.assertEqual(len(disp), 28)
		self.assertEqual(len(disp.split('\n')), 10)
		
	def test_display_log_with_three_messages(self):
		self.e.insert('Three\nline\nmessage')
		disp = self.e.display_log().strip()
		self.assertEqual(len(disp.split('\n')), 10)
		self.assertEqual(disp.split('\n')[0], '* ')
		self.assertEqual(disp.split('\n')[7], '* Three')
		self.assertEqual(disp.split('\n')[8], '* line')
		self.assertEqual(disp.split('\n')[9], '* message')
		
	def test_display_log_with_eleven_messages(self):
		self.e.insert('one\ntwo\nthree\nfour\nfive\nsix\nseven\neight\nnine\nten\neleven')
		disp = self.e.display_log().strip()
		self.assertEqual(self.e.length, 11)
		self.assertEqual(len(disp.split('\n')), 10)
		self.assertEqual(disp.split('\n')[0], '* two')
		self.assertEqual(disp.split('\n')[9], '* eleven')


if __name__ == '__main__':
    unittest.main()
