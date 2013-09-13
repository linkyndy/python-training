import time

def timer(threshold=9999):
	def wrap(func):
		def inner(*args, **kwargs):
			start = time.time()
			ret = func(*args, **kwargs)
			end = time.time()
			print 'Function {name} took {time:.4f}s ({thres} ' \
				  'threshold)'.format(name=func.__name__, time=end-start, \
				  thres='within' if (end-start) < threshold else 'not in')
			return ret
		return inner
	return wrap
