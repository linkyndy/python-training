class ModelBase(type):

	attrs = set()

	def __new__(cls, name, bases, attrs):
		for attr in attrs:
			cls.attrs |= set([attr])
		
		return super(ModelBase, cls).__new__(cls, name, bases, attrs)


class Model(object):
	__metaclass__ = ModelBase


class Person(Model):
	name = 'John Doe'
	age = 50


class Field(object):
	pass


class IntegerField(Field):
	pass


class StringField(Field):
	pass