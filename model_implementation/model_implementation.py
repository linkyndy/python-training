class ModelBase(type):

	attrs = set()

	def __new__(cls, name, bases, attrs):
		for attr in attrs:
			cls.attrs |= set([attr])
		
		return super(ModelBase, cls).__new__(cls, name, bases, attrs)


class Model(object):
	__metaclass__ = ModelBase

	def sql(self):
		pass


class Field(object):
	def __init__(self):
		pass

class IntegerField(Field):
	def __init__(self, *args, **kwargs):
		super(IntegerField, self).__init__(*args, **kwargs)

	def get_field_type(self):
		return 'IntegerField'

	def get_default_value(self):
		return 0


class StringField(Field):
	def __init__(self, *args, **kwargs):
		super(StringField, self).__init__(*args, **kwargs)

	def get_field_type(self):
		return 'StringField'

	def get_default_value(self):
		return ''


class Person(Model):
	name = StringField()
	age = IntegerField()