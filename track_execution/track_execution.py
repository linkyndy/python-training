import time

output = 'Function {name} took {time:.4f}s ({thres} threshold)'


def timer(threshold=9999):
    def wrapper(func):
        def inner(*args, **kwargs):
            start = time.time()
            ret = func(*args, **kwargs)
            end = time.time()
            print output.format(
                name=func.__name__,
                time=end-start,
                thres='within' if (end-start) < threshold else 'not in')
            return ret
        return inner
    return wrapper
