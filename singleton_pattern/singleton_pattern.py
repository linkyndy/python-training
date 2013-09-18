class Singleton(type):
	"""Metaclass which implements the singleton pattern"""

	_instances = {}

	def __call__(self, *args, **kwargs):
		if self not in self._instances:
			self._instances[self] = super(Singleton, self).__call__(*args, **kwargs)
		return self._instances[self]

	def __copy__(self, *args, **kwargs):
		return self._instances[self]
