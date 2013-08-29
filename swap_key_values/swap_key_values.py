def swap_key_values(d):
	"""Swap key with values in a dictionary if it is possible"""

	def valid_key(key):
		"""Checks whether the parameter is a valid key"""

		if (isinstance(key, int) or 
		   isinstance(key, float) or 
		   isinstance(key, long) or 
		   isinstance(key, complex) or
		   isinstance(key, basestring)):
			return True
		elif isinstance(key, tuple):
			for item in key:
				if not valid_key(item):
					return False
			return True
		else:
			return False

	e = {}

	for key, value in d.iteritems():
		if not valid_key(value):
			return False
		e[value] = key

	return e
