from collections import OrderedDict


def sort_dictionaries(infile, outfile):
    """Sort dictionaries read from a file and print their id in another file"""

    def from_file(filename):
        """Converts a file with a specified format to dictionaries"""

        # Holds the dictionaries together with their insert order
        dicts = OrderedDict()

        # Holds the id of the currently parsed dictionary
        dict_id = 1

        # Holds the currently parsed dictionary
        d = OrderedDict()

        for line in open(filename):
            # Start a new dictionary after each empty line; else
            # append key-value pair to current dictionary
            if line == '\n':
                dicts[dict_id] = d
                dict_id += 1
                d = OrderedDict()
            else:
                key, val = line.split()
                d[key] = val

        dicts[dict_id] = d

        return dicts

    def sort_dicts(dicts):
        """Sorts a dictionary list by a specified algorithm"""

        def compare(a, b):
            """Compares dictionary values"""

            # Get the two dictionaries' values
            av = a[1].values()
            bv = b[1].values()

            # Compare values present in both dictionaries; if
            # elements differ, return their compared values
            for i in range(min(len(av), len(bv))):
                if av[i] != bv[i]:
                    return cmp(av[i], bv[i])

            # Should reach this line only if all values present in both
            # dictionaries are equal between them; in this case, the
            # dictionary with fewer elements is the smallest one
            return 1 if len(av) > len(bv) else -1

        # Sort each OrderedDict by key ascending
        for order, dictionary in dicts.iteritems():
            dicts[order] = OrderedDict(sorted(dictionary.items(),
                                              key=lambda k: k[0]))

        # Sort and return the OrderedDict by the cmp function
        return sorted(dicts.items(), cmp=compare)

    def to_file(filename, dicts):
        """Writes a list of dictionary ids to a file"""

        with open(filename, "w") as f:
            for order, dictionary in dicts:
                f.write("%s " % order)

    dicts = from_file(infile)
    dicts = sort_dicts(dicts)
    to_file(outfile, dicts)
