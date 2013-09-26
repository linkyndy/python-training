from metaclass_model_implementation import ModelBase, Model, Field, StringField, IntegerField
import unittest


class ModelBaseTests(unittest.TestCase):
    """Various model base tests"""

    def setUp(self):
        class TestModel(Model):
            int_field = IntegerField()
            string_field = StringField()

        self.test_model = TestModel

    def testFieldsDictPresent(self):
        self.assertTrue(hasattr(self.test_model, 'fields'))

    def testAllFieldsPresent(self):
        self.assertEqual(len(self.test_model.fields), 2)
        self.assertIn('int_field', self.test_model.fields)
        self.assertIn('string_field', self.test_model.fields)


class ModelTests(unittest.TestCase):
    """Various model tests"""

    def setUp(self):
        class TestModel(Model):
            int_field = IntegerField()
            string_field = StringField()

        self.test_model = TestModel

    def testKwargsSet(self):
        test_object = self.test_model(string_field='test', int_field=1)
        self.assertTrue(hasattr(test_object, 'string_field'))
        self.assertTrue(hasattr(test_object, 'int_field'))
        self.assertEqual(test_object.string_field, 'test')
        self.assertEqual(test_object.int_field, 1)

    def testTooManyKwargs(self):
        self.assertRaises(IndexError,
                          self.test_model,
                          string_field='test', int_field=1, extra=2)

    def testDefaultValueUse(self):
        test_object = self.test_model()
        self.assertEqual(test_object.string_field, '')
        self.assertEqual(test_object.int_field, 0)


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
        self.assertRaises(AttributeError, self.integer_field.validate, 'str')


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
