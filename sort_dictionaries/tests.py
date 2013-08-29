from sort_dictionaries import sort_dictionaries as f
import unittest
import os

class SortDictionariesTests(unittest.TestCase):
	"""Various inputs for the dictionary sorting function"""

	def testOne(self):
		data = 'a 1\nb 2\n\nb 0\na 9'
		expected = '1 2 '

		g = open('in.txt', 'w')
		g.write(data)
		g.close()

		f('in.txt', 'out.txt')

		h = open('out.txt')
		self.assertEqual(h.read(), expected)

		os.remove('in.txt')
		os.remove('out.txt')

	def testTwo(self):
		data = 'b 1\nc 2\n\nb 0\na 9'
		expected = '1 2 '

		g = open('in.txt', 'w')
		g.write(data)
		g.close()

		f('in.txt', 'out.txt')

		h = open('out.txt')
		self.assertEqual(h.read(), expected)

		os.remove('in.txt')
		os.remove('out.txt')

	def testThree(self):
		data = 'b 1\nc 2\n\nb 1\nc 2'
		expected = '2 1 '

		g = open('in.txt', 'w')
		g.write(data)
		g.close()

		f('in.txt', 'out.txt')

		h = open('out.txt')
		self.assertEqual(h.read(), expected)

		os.remove('in.txt')
		os.remove('out.txt')

	def testFour(self):
		data = 'b 1\nc 2'
		expected = '1 '

		g = open('in.txt', 'w')
		g.write(data)
		g.close()

		f('in.txt', 'out.txt')

		h = open('out.txt')
		self.assertEqual(h.read(), expected)

		os.remove('in.txt')
		os.remove('out.txt')

def main():
	unittest.main()

if __name__ == '__main__':
	main()