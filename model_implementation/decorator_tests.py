from decorator_model_implementation import modellize, string_field, integer_field
import unittest


class StringFieldTests(unittest.TestCase):
	"""Various tests for string_field"""

	def testNoValue(self):
		self.assertEqual(string_field(), '')

	def testStringValue(self):
		self.assertEqual(string_field('string'), 'string')

	def testAnyValue(self):
		self.assertEqual(string_field(34), '34')


class IntegerFieldTests(unittest.TestCase):
	"""Various tests for integer_field"""

	def testNoValue(self):
		self.assertEqual(integer_field(), 0)

	def testIntegerValue(self):
		self.assertEqual(integer_field(10), 10)

	def testStringValue(self):
		self.assertEqual(integer_field('10'), 10)

	def testInvalidValue(self):
		self.assertRaises(AttributeError, integer_field, 'string')


class ModellizeTests(unittest.TestCase):
	"""Various tests for modellize decorator"""

	def setUp(self):
		@modellize
		def person(**kwargs):
			return {'test_string': 'string_field',
			        'test_integer': 'integer_field'}
		self.model = person

	def testAllFieldsInDict(self):
		person = self.model()
		self.assertEqual(len(person), 2)
		self.assertIn('test_string', person)
		self.assertIn('test_integer', person)

	def testKwargsSet(self):
		person = self.model(test_string='string', test_integer=1)
		self.assertEqual(person['test_string'], 'string')
		self.assertEqual(person['test_integer'], 1)

	def testDefaultValues(self):
		person = self.model()
		self.assertEqual(person['test_string'], '')
		self.assertEqual(person['test_integer'], 0)


def main():
	unittest.main()

if __name__ == '__main__':
	main()