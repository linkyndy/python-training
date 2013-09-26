import decorator_field_types


def modellize(func):
    """Decorator which makes any function act like a model"""

    def process(**kwargs):
        """
        Build a dictionary with the model's declared fields, then
        bind the given values from the function call to these fields"""

        fields = {}
        for field, field_type in func().iteritems():
            field_func = getattr(decorator_field_types, field_type)
            fields[field] = field_func(kwargs[field]) if field in kwargs else field_func()
        return fields
    return process
