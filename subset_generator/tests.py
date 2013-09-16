from subset_generator import subset_generator as f
import unittest

class GeneratorTests(unittest.TestCase):
	"""Various generator tests"""

	def testEmptySet(self):
		s = set()
		subsets = []
		expected = [set()]

		for elem in f(s):
			subsets.append(elem)

		self.assertEqual(subsets, expected)

	def testAnotherEmptySet(self):
		s = set([])
		subsets = []
		expected = [set([])]

		for elem in f(s):
			subsets.append(elem)

		self.assertEqual(subsets, expected)

	def testOneElementSet(self):
		s = set([1])
		subsets = []
		expected = [set([]), set([1])]

		for elem in f(s):
			subsets.append(elem)

		self.assertEqual(subsets, expected)

	def testTwoElementSet(self):
		s = set([1, 2])
		subsets = []
		expected = [set([]), set([1]), set([2]), set([1, 2])]

		for elem in f(s):
			subsets.append(elem)

		self.assertEqual(subsets, expected)

def main():
	unittest.main()

if __name__ == '__main__':
	main()