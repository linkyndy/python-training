from flatten_two_lists import flatten_two_lists
import unittest


class EmptyListsTests(unittest.TestCase):
    """Both lists empty, various depth"""

    def setUp(self):
        self.a = self.b = []

    def testNoDepth(self):
        expected = ([], [])
        self.assertEqual(flatten_two_lists(self.a, self.b, 0), expected)

    def testOneDepth(self):
        expected = ([], [])
        self.assertEqual(flatten_two_lists(self.a, self.b, 1), expected)

    def testRandomDepth(self):
        expected = ([], [])
        self.assertEqual(flatten_two_lists(self.a, self.b, 195667), expected)

    def testNegativeDepth(self):
        expected = ([], [])
        self.assertEqual(flatten_two_lists(self.a, self.b, -345), expected)


class SingleElementListsTests(unittest.TestCase):
    """Both lists of one element, various depth"""

    def setUp(self):
        self.a = [1]
        self.b = [2]

    def testNoDepth(self):
        expected = ([1], [2])
        self.assertEqual(flatten_two_lists(self.a, self.b, 0), expected)

    def testOneDepth(self):
        expected = ([1], [2])
        self.assertEqual(flatten_two_lists(self.a, self.b, 1), expected)

    def testRandomDepth(self):
        expected = ([1], [2])
        self.assertEqual(flatten_two_lists(self.a, self.b, 456756), expected)

    def testNegativeDepth(self):
        expected = ([1], [2])
        self.assertEqual(flatten_two_lists(self.a, self.b, -456), expected)


class MultiElementListsTests(unittest.TestCase):
    """Simple lists with more than one element, various depth"""

    def setUp(self):
        self.a = [1, 2, 3]
        self.b = [4, 5]

    def testNoDepth(self):
        expected = ([1, 2, 3], [4, 5])
        self.assertEqual(flatten_two_lists(self.a, self.b, 0), expected)

    def testOneDepth(self):
        expected = ([1, 2, 3], [4, 5])
        self.assertEqual(flatten_two_lists(self.a, self.b, 1), expected)

    def testRandomDepth(self):
        expected = ([1, 2, 3], [4, 5])
        self.assertEqual(flatten_two_lists(self.a, self.b, 456565), expected)

    def testNegativeDepth(self):
        expected = ([1, 2, 3], [4, 5])
        self.assertEqual(flatten_two_lists(self.a, self.b, -346), expected)


class CombinedElementListsTests(unittest.TestCase):
    """Simple lists with various elements, various depth"""

    def testNoOneElementsNoDepth(self):
        a = []
        b = [1]
        expected = ([], [1])
        self.assertEqual(flatten_two_lists(a, b, 0), expected)

    def testNoOneElementsRandomDepth(self):
        a = []
        b = [1]
        expected = ([], [1])
        self.assertEqual(flatten_two_lists(a, b, 456784), expected)

    def testNoOneElementsNegativeDepth(self):
        a = []
        b = [1]
        expected = ([], [1])
        self.assertEqual(flatten_two_lists(a, b, -834), expected)

    def testNoMultiElementsNoDepth(self):
        a = []
        b = [1, 2, 3]
        expected = ([], [1, 2, 3])
        self.assertEqual(flatten_two_lists(a, b, 0), expected)

    def testNoMultiElementsRandomDepth(self):
        a = []
        b = [1, 2, 3]
        expected = ([], [1, 2, 3])
        self.assertEqual(flatten_two_lists(a, b, 347658), expected)

    def testNoMultiElementsNegativeDepth(self):
        a = []
        b = [1, 2, 3]
        expected = ([], [1, 2, 3])
        self.assertEqual(flatten_two_lists(a, b, -589), expected)

    def testOneMultiElementsNoDepth(self):
        a = [1]
        b = [2, 3]
        expected = ([1], [2, 3])
        self.assertEqual(flatten_two_lists(a, b, 0), expected)

    def testOneMultiElementsRandomDepth(self):
        a = [1]
        b = [2, 3]
        expected = ([1], [2, 3])
        self.assertEqual(flatten_two_lists(a, b, 456777), expected)

    def testOneMultiElementsNegativeDepth(self):
        a = [1]
        b = [2, 3]
        expected = ([1], [2, 3])
        self.assertEqual(flatten_two_lists(a, b, -476), expected)


class LayeredListsTests(unittest.TestCase):
    """Layered lists with various elements, various depth"""

    def testOneLayerNoDepth(self):
        a = [1, [2], 3]
        b = [4, [5], 6]
        expected = ([1, [2], 3], [4, [5], 6])
        self.assertEqual(flatten_two_lists(a, b, 0), expected)

    def testOneLayerOneDepth(self):
        a = [1, [2], 3]
        b = [4, [5], 6]
        expected = ([1, 2, 3], [4, 5, 6])
        self.assertEqual(flatten_two_lists(a, b, 1), expected)

    def testOneLayerRandomDepth(self):
        a = [1, [2], 3]
        b = [4, [5], 6]
        expected = ([1, 2, 3], [4, 5, 6])
        self.assertEqual(flatten_two_lists(a, b, 157869), expected)

    def testOneLayerNegativeDepth(self):
        a = [1, [2], 3]
        b = [4, [5], 6]
        expected = ([1, [2], 3], [4, [5], 6])
        self.assertEqual(flatten_two_lists(a, b, -577), expected)

    def testMultiLayerNoDepth(self):
        a = [1, [2, [3, 4], [5]], 6, [7]]
        b = [8, [[9], []], []]
        expected = ([1, [2, [3, 4], [5]], 6, [7]], [8, [[9], []], []])
        self.assertEqual(flatten_two_lists(a, b, 0), expected)

    def testMultiLayerOneDepth(self):
        a = [1, [2, [3, 4], [5]], 6, [7]]
        b = [8, [[9], []], []]
        expected = ([1, 2, [3, 4], [5], 6, 7], [8, [9], []])
        self.assertEqual(flatten_two_lists(a, b, 1), expected)

    def testMultiLayerRandomDepth(self):
        a = [1, [2, [3, 4], [5]], 6, [7]]
        b = [8, [[9], []], []]
        expected = ([1, 2, 3, 4, 5, 6, 7], [8, 9])
        self.assertEqual(flatten_two_lists(a, b, 849633), expected)

    def testMultiLayerNegativeDepth(self):
        a = [1, [2, [3, 4], [5]], 6, [7]]
        b = [8, [[9], []], []]
        expected = ([1, [2, [3, 4], [5]], 6, [7]], [8, [[9], []], []])
        self.assertEqual(flatten_two_lists(a, b, -561), expected)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
