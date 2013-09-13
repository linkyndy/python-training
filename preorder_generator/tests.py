from preorder_generator import preorder_generator as f
import unittest

class GeneratorTests(unittest.TestCase):
	"""Various generator tests"""

	def testEmptyTree(self):
		tree = ()
		nodes = []
		expected = []

		for node in f(tree):
			nodes.append(node)

		self.assertEqual(nodes, expected)

	def testSingleNodeTree(self):
		tree = ('a', None, None)
		nodes = []
		expected = ['a']

		for node in f(tree):
			nodes.append(node)

		self.assertEqual(nodes, expected)

	def testTwoNodeTree(self):
		tree = ('a', ('b', None, None), None)
		nodes = []
		expected = ['a', 'b']

		for node in f(tree):
			nodes.append(node)

		self.assertEqual(nodes, expected)

	def testAnotherTwoNodeTree(self):
		tree = ('a', None, ('b', None, None))
		nodes = []
		expected = ['a', 'b']

		for node in f(tree):
			nodes.append(node)

		self.assertEqual(nodes, expected)

	def testThreeNodeTree(self):
		tree = ('a', ('b', None, None), ('c', None, None))
		nodes = []
		expected = ['a', 'b', 'c']

		for node in f(tree):
			nodes.append(node)

		self.assertEqual(nodes, expected)

	def testMultiNodeTree(self):
		tree = ('a', ('b', ('c', None, None), None), ('d', None, ('e', None, None)))
		nodes = []
		expected = ['a', 'b', 'c', 'd', 'e']

		for node in f(tree):
			nodes.append(node)

		self.assertEqual(nodes, expected)

	def testAnotherMultiNodeTree(self):
		tree = ('a', ('b', ('c', None, None), None), None)
		nodes = []
		expected = ['a', 'b', 'c']

		for node in f(tree):
			nodes.append(node)

		self.assertEqual(nodes, expected)

def main():
	unittest.main()

if __name__ == '__main__':
	main()