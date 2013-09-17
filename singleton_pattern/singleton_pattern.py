class Singleton(type):
	_instances = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

class Test(object):
	__metaclass__ = Singleton

	@classmethod
	def p(cls):
		return cls._instances

class AnotherTest(object):
	__metaclass__ = Singleton

	@classmethod
	def p(cls):
		return cls._instances

if __name__ == '__main__':
	t = Test()
	u = Test()
	print t.p()
	print u.p()
	v = AnotherTest()
	w = AnotherTest()
	print v.p()
	print w.p()