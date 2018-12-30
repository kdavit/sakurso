import unittest
from classes.stack import Stack

class TestStack(unittest.TestCase):

	def test_push_X_get_size(self):
		result = Stack(3)
		result.push("5")
		result.push("4")
		self.assertEqual(result.get_size(),2)

	def test_has_space(self):
		result = Stack(2)
		result.push(2)
		self.assertTrue(result.has_space())

	def test_peek(self):
		result = Stack(0)
		self.assertIsNone(result.peek())
		result.push("madara")
		self.assertIsNotNone(result.peek())

	def test_is_empty(self):
		result = Stack(2)
		self.assertTrue(result)
		result.push("dio")
		self.assertFalse(result.is_empty())

	def test_get_name(self):
		result = Stack("madara")
		self.assertEqual(result.get_name(),"madara")

	def test_pop(self):
		result = Stack(2)
		self.assertIsNone(result.pop())
		result.push(2)
		result.push(5)
		result.pop()
		self.assertEqual(result.get_size(),1)
		self.assertEqual(result.pop(),2)



if __name__ == '__main__':
	unittest.main()
