class ModelBase(type):
	"""Base type for created models"""

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
		# Only add attrs declared as fields
		for attr, val in attrs.iteritems():
			if isinstance(val, Field):
				new_class.add_to_class(attr, val)
		
		return new_class

	def add_to_class(cls, attr, val):
		"""Add an attribute to class' fields dictionary"""
		
		getattr(cls, 'fields')[attr] = val


class Model(object):
	"""Base class for created objects"""

	__metaclass__ = ModelBase

	def __init__(self, **kwargs):
		# Check the supplied number of kwargs
		if len(kwargs) > len(self.fields):
			raise IndexError('Too many arguments supplied to model')

		# For each declared model field attach supplied kwarg
		# or default field value
		# Perform validation also
		for field, field_type in self.fields.iteritems():
			val = kwargs.pop(field, field_type.get_default_value())
			setattr(self, field, field_type.validate(val))


class Field(object):
	def __init__(self, max_length=None):
		self.max_length = max_length

	def validate(self, value):
		"""Should be overridden by subclasses to provide validation"""

		pass


class IntegerField(Field):
	def __init__(self, *args, **kwargs):
		super(IntegerField, self).__init__(*args, **kwargs)

	def get_default_value(self):
		return 0

	def validate(self, val):
		try:
			return int(val)
		except:
			raise AttributeError('Invalid value for IntegerField')


class StringField(Field):
	def __init__(self, *args, **kwargs):
		super(StringField, self).__init__(*args, **kwargs)

	def get_default_value(self):
		return ''

	def validate(self, val):
		try:
			return str(val)
		except:
			raise AttributeError('Invalid value for StringField')