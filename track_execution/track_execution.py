import time
import inspect


def timer(func, threshold=0):
	def inner(*args, **kwargs):
		start = time.clock()
		ret = func(*args, **kwargs)
		end = time.clock()
		print 'Function ', inspect.stack()[1][3], ' took ', (end - start), 's'
		return ret
	return inner

@timer
def function():
	pass

@timer
def longfunction():
	a = []
	for i in range(0,10000000):
		a.append(i)

if __name__ == '__main__':
	function()
	longfunction()