from model_implementation import ModelBase, Model, Field, StringField, IntegerField
import unittest

class ModelBaseTests(unittest.TestCase):
	"""Various model tests"""

	def setUp(self):
		class TestModel(object):
			__metaclass__ = ModelBase
			int_field = IntegerField()
		
		self.test_model = TestModel

		class Model(object):
			__metaclass__ = ModelBase

		self.model = Model

	def testFieldsDictPresent(self):
		self.assertTrue(hasattr(self.test_model, 'fields'))

	def testFieldsDictNotPresent(self):
		self.assertFalse(hasattr(self.model, 'fields'))

class ModelTests(unittest.TestCase):
	"""Various model tests"""

	pass 


class FieldTests(unittest.TestCase):
	"""Various model tests"""

	def testNoMaxLength(self):
		field = Field()
		self.assertEqual(field.max_length, None)

	def testSpecifiedMaxLength(self):
		field = Field(max_length=50)
		self.assertEqual(field.max_length, 50) 

class IntegerFieldTests(unittest.TestCase):
	"""Various integer field tests"""

	def setUp(self):
		self.integer_field = IntegerField()

	def testDefaultValue(self):
		self.assertEqual(self.integer_field.get_default_value(), 0)

	def testValidateInt(self):
		self.assertEqual(self.integer_field.validate(10), 10)

	def testValidateCastInt(self):
		self.assertEqual(self.integer_field.validate('10'), 10)

	def testValidateOther(self):
		self.assertRaises(AttributeError, self.integer_field.validate, 'string')

class StringFieldTests(unittest.TestCase):
	"""Various string field tests"""

	def setUp(self):
		self.string_field = StringField()

	def testDefaultValue(self):
		self.assertEqual(self.string_field.get_default_value(), '')

	def testValidateString(self):
		self.assertEqual(self.string_field.validate('string'), 'string')

	def testValidateCastInt(self):
		self.assertEqual(self.string_field.validate(10), '10')


def main():
	unittest.main()

if __name__ == '__main__':
	main()