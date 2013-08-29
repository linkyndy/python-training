from swap_key_values import swap_key_values as f
import unittest

class SwapKeyValuesTests(unittest.TestCase):
	"""Tests for valid dictionary key types"""

	def testInt(self):
		a = {'a': 1, 'b': 2}
		expected = {1: 'a', 2: 'b'}
		self.assertEqual(f(a), expected)

	def testLong(self):
		a = {'a': 1L, 'b': 2L}
		expected = {1L: 'a', 2L: 'b'}
		self.assertEqual(f(a), expected)

	def testFloat(self):
		a = {'a': 1.0, 'b': 2.0}
		expected = {1.0: 'a', 2.0: 'b'}
		self.assertEqual(f(a), expected)

	def testComplex(self):
		a = {'a': 1+2j, 'b': 2+3j}
		expected = {1+2j: 'a', 2+3j: 'b'}
		self.assertEqual(f(a), expected)

	def testString(self):
		a = {'a': 'abc', 'b': 'def'}
		expected = {'abc': 'a', 'def': 'b'}
		self.assertEqual(f(a), expected)

	def testTuple(self):
		a = {'a': (1, 2), 'b': (3, 4)}
		expected = {(1, 2): 'a', (3, 4): 'b'}
		self.assertEqual(f(a), expected)

	def testNestedTuple(self):
		a = {'a': (1, (2)), 'b': ((3), 4)}
		expected = {(1, (2)): 'a', ((3), 4): 'b'}
		self.assertEqual(f(a), expected)

	def testComplexTuple(self):
		a = {'a': (1, ('abc', ()), ''), 'b': (((), ''), (3), 'def')}
		expected = {(1, ('abc', ()), ''): 'a', (((), ''), (3), 'def'): 'b'}
		self.assertEqual(f(a), expected)

class SwapKeyValuesInvalidTests(unittest.TestCase):
	"""Tests for invalid dictionary key types"""

	def testList(self):
		a = {'a': [1, 2, 3]}
		self.assertFalse(f(a))

	def testNestedList(self):
		a = {'a': [1, 2, [3]]}
		self.assertFalse(f(a))

	def testDictionary(self):
		a = {'a': {'b': 1, 'c': 2}}
		self.assertFalse(f(a))

	def testNestedDictionary(self):
		a = {'a': {'b': {'c': 1}}}
		self.assertFalse(f(a))

	def testTupleOne(self):
		a = {'a': (1, [2])}
		self.assertFalse(f(a))

	def testTupleTwo(self):
		a = {'a': (1, {'a': 2})}
		self.assertFalse(f(a))

def main():
	unittest.main()

if __name__ == '__main__':
	main()