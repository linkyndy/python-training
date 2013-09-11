from card_dealer import Deck, Player, Dealer
import unittest

class DeckTests(unittest.TestCase):
	"""Tests decks"""

	def setUp(self):
		self.deck = Deck()

	def testNumberOfCards(self):
		self.assertEqual(len(self.deck.cards), 52)


class PlayerTests(unittest.TestCase):
	"""Tests players"""

	def testPlayerName(self):
		p = Player('John')
		self.assertEqual(str(p), 'John')

class DealerTests(unittest.TestCase):
	"""Tests dealers"""

	def testDealerName(self):
		d = Dealer('Jane')
		self.assertEqual(str(d), 'Jane')


def main():
	unittest.main()

if __name__ == '__main__':
	main()