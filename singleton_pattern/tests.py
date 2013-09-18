from singleton_pattern import Singleton
import unittest
import copy

class SingletonTests(unittest.TestCase):
	"""Various singleton tests"""

	def setUp(self):
		class Test(object):
			__metaclass__ = Singleton
		self.test = Test

		class AnotherTest(object):
			__metaclass__ = Singleton
		self.another_test = AnotherTest

	def testTwoObjectsSameClass(self):
		a = self.test()
		b = self.test()
		self.assertEqual(id(a), id(b))

	def testTwoObjectsAssignment(self):
		a = self.test()
		b = a
		self.assertEqual(id(a), id(b))

	def testTwoObjectsCopy(self):
		a = self.test()
		b = copy.copy(a)
		self.assertEqual(id(a), id(b))

	def testTwoObjectsDifferentClass(self):
		a = self.test()
		b = self.another_test()
		self.assertNotEqual(id(a), id(b))

def main():
	unittest.main()

if __name__ == '__main__':
	main()