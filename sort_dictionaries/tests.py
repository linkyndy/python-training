from sort_dictionaries import sort_dictionaries as f
import unittest
from tempfile import NamedTemporaryFile

class SortDictionariesTests(unittest.TestCase):
	"""Various inputs for the dictionary sorting function"""

	def testOne(self):
		data = 'a 1\nb 2\n\nb 0\na 9'
		expected = '1 2'
		with NamedTemporaryFile() as infile, NamedTemporaryFile() as outfile:
			infile.write(data)
			f(infile.name, outfile.name)
			self.assertEqual(outfile.read(), expected)

	def testTwo(self):
		data = 'b 1\nc 2\n\nb 0\na 9'
		expected = '1 2'
		with NamedTemporaryFile() as infile, NamedTemporaryFile() as outfile:
			infile.write(data)
			f(infile.name, outfile.name)
			self.assertEqual(outfile.read(), expected)

	def testThree(self):
		data = 'b 1\nc 2\n\nb 1\nc 2'
		expected = '1 2'
		with NamedTemporaryFile() as infile, NamedTemporaryFile() as outfile:
			infile.write(data)
			f(infile.name, outfile.name)
			self.assertEqual(outfile.read(), expected)

def main():
	unittest.main()

if __name__ == '__main__':
	main()