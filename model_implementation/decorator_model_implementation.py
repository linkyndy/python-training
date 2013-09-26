def string_field(val=''):
	"""Wrapper for string fields"""

	try:
		return str(val)
	except:
		raise AttributeError('Invalid value for string_field')

def integer_field(val=0):
	"""Wrapper for integer fields"""

	try:
		return int(val)
	except:
		raise AttributeError('Invalid value for integer_field')

def modellize(func):
	"""Decorator which makes any function act like a model"""

	def process(**kwargs):
		"""
		Build a dictionary with the model's declared fields, then
		bind the given values from the function call to these fields"""

		fields = {}
		for field, field_type in func().iteritems():
			field_func = globals()[field_type]
			fields[field] = field_func(kwargs[field]) if field in kwargs else field_func()
		return fields
	return process

@modellize
def person(**kwargs):
	return {'name': 'string_field',
		    'age': 'integer_field'}
