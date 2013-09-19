def merge_two_objects(a, b):
    """Merge two objects up to any depth"""

    while len(a) > 0:
        key, value = a.popitem()

        if key in b:
            if type(value) != type(b[key]):
                b[key] = (value, b[key])
            elif isinstance(value, dict):
                b[key] = merge_two_objects(value, b[key])
            elif isinstance(value, set):
                b[key] = value.union(b[key])
            else:
                b[key] = value + b[key]
        else:
            b[key] = value

    return b
