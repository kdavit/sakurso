import unittest
from classes.node import Node

class TestStack(unittest.TestCase):

	def test_get_value(self):
		result = Node(5)
		self.assertEqual(result.get_value(),5)

	def test_set_link_node(self):
		node1 = Node("dio")
		node2 = Node("jonathan")
		node3 = Node("giorno")
		node1.set_link_node(node2)
		node3.set_link_node(node1)
		node1_data = node3.get_link_node().get_value()
		node2_data = node1.get_link_node().get_value()
		self.assertNotEqual(node1_data, node2_data)

	def test_get_link_node(self):
		node1 = Node("1")
		node2 = Node("2")
		node1.set_link_node(node2)
		result = node2.get_link_node()
		self.assertIsNone(result)




if __name__ == '__main__':
	unittest.main()