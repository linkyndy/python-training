from subset_generator import subset_generator
import unittest


class GeneratorTests(unittest.TestCase):
    """Various generator tests"""

    def testEmptySet(self):
        s = set()
        expected = [set()]

        self.assertEqual([e for e in subset_generator(s)], expected)

    def testAnotherEmptySet(self):
        s = set([])
        expected = [set([])]

        self.assertEqual([e for e in subset_generator(s)], expected)

    def testOneElementSet(self):
        s = set([1])
        expected = [set([]), set([1])]

        self.assertEqual([e for e in subset_generator(s)], expected)

    def testTwoElementSet(self):
        s = set([1, 2])
        expected = [set([]), set([1]), set([2]), set([1, 2])]

        self.assertEqual([e for e in subset_generator(s)], expected)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
