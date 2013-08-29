from merge_two_objects import merge_two_objects as f
import unittest

class MergeTwoObjectsTests(unittest.TestCase):

	def testEmptyObjects(self):
		a = b = {}
		expected = {}
		self.assertEqual(f(a, b), expected)

	def testIntObjects(self):
		a = {'key': 1}
		b = {'key': 2}
		expected = {'key': 3}
		self.assertEqual(f(a, b), expected)

	def testFloatObjects(self):
		a = {'key': 1.0}
		b = {'key': 2.0}
		expected = {'key': 3.0}
		self.assertEqual(f(a, b), expected)

	def testStringObjects(self):
		a = {'key': 'abc'}
		b = {'key': 'def'}
		expected = {'key': 'abcdef'}
		self.assertEqual(f(a, b), expected)

	def testTupleObjects(self):
		a = {'key': (1, 2)}
		b = {'key': (3, 4)}
		expected = {'key': (1, 2, 3, 4)}
		self.assertEqual(f(a, b), expected)

	def testListObjects(self):
		a = {'key': [1, 2]}
		b = {'key': [3, 4]}
		expected = {'key': [1, 2, 3, 4]}
		self.assertEqual(f(a, b), expected)

	def testSetObjects(self):
		a = {'key': set([1, 2])}
		b = {'key': set([3, 4])}
		expected = {'key': set([1, 2, 3, 4])}
		self.assertEqual(f(a, b), expected)

	def testDictionaryObjects(self):
		a = {'key': {'inner_key': 1}}
		b = {'key': {'inner_key': 2}}
		expected = {'key': {'inner_key': 3}}
		self.assertEqual(f(a, b), expected)

	def testMultiDictionaryObjects(self):
		a = {'key': {'inner_key': 1, 'another_key': 2}}
		b = {'key': {'inner_key': 2, 'another_key': 3}}
		expected = {'key': {'inner_key': 3, 'another_key': 5}}
		self.assertEqual(f(a, b), expected)

	def testDifferentTypeObjects(self):
		a = {'key': 1}
		b = {'key': 'abc'}
		expected = {'key': (1, 'abc')}
		self.assertEqual(f(a, b), expected)

def main():
	unittest.main()

if __name__ == '__main__':
	main()