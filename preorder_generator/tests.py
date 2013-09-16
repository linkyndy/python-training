from preorder_generator import preorder_generator as f
import unittest

class GeneratorTests(unittest.TestCase):
	"""Various generator tests"""

	def testEmptyTree(self):
		tree = ()
		expected = []

		self.assertEqual([x for x in f(tree)], expected)

	def testSingleNodeTree(self):
		tree = ('a', None, None)
		expected = ['a']

		self.assertEqual([x for x in f(tree)], expected)

	def testTwoNodeTree(self):
		tree = ('a', ('b', None, None), None)
		expected = ['a', 'b']

		self.assertEqual([x for x in f(tree)], expected)

	def testAnotherTwoNodeTree(self):
		tree = ('a', None, ('b', None, None))
		expected = ['a', 'b']

		self.assertEqual([x for x in f(tree)], expected)

	def testThreeNodeTree(self):
		tree = ('a', ('b', None, None), ('c', None, None))
		expected = ['a', 'b', 'c']

		self.assertEqual([x for x in f(tree)], expected)

	def testMultiNodeTree(self):
		tree = ('a', ('b', ('c', None, None), None), ('d', None, ('e', None, None)))
		expected = ['a', 'b', 'c', 'd', 'e']

		self.assertEqual([x for x in f(tree)], expected)

	def testAnotherMultiNodeTree(self):
		tree = ('a', ('b', ('c', None, None), None), None)
		expected = ['a', 'b', 'c']

		self.assertEqual([x for x in f(tree)], expected)

def main():
	unittest.main()

if __name__ == '__main__':
	main()