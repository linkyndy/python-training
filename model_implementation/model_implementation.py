class ModelBase(type):

	def __new__(cls, name, bases, attrs):
		super_new = super(ModelBase, cls).__new__

		# Don't add fields for base class Model
		if name == 'Model':
			return super_new(cls, name, bases, attrs)

		module = attrs['__module__']
		new_class = super_new(cls, name, bases, {'__module__': module})

		# Initialize fields dictionary on new class
		setattr(new_class, 'fields', {})

		# Add attrs to new class' fields dictionary
		for attr, val in attrs.iteritems():
			new_class.add_to_class(attr, val)
		
		return new_class

	def add_to_class(cls, attr, val):
		"""Add an attribute to class' fields dictionary"""
		
		getattr(cls, 'fields')[attr] = val


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