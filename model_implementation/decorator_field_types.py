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