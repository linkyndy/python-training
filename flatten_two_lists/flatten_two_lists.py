def flatten_two_lists(a, b, depth):
    """Flatten two lists up to depth"""

    def flatten(l, depth):
        """Recursively flatten list up to depth"""

        if isinstance(l, list):
            if depth <= 0:
                return l
            if len(l) == 0:
                return []

            first, rest = l[0], l[1:]
            return flatten(first, depth - 1) + flatten(rest, depth)
        else:
            return [l]

    return flatten(a, depth), flatten(b, depth)
