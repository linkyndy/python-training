from card_dealer import Card, Deck, Hand, Player, Dealer, Game
import unittest


class CardTests(unittest.TestCase):
	"""Tests cards"""

	def testCardOutput(self):
		c = Card(14)
		self.assertEqual(str(c), u'3\u2663'.encode('utf-8'))

class DeckTests(unittest.TestCase):
	"""Tests decks"""

	def setUp(self):
		self.deck = Deck()

	def testNumberOfCards(self):
		self.assertEqual(len(self.deck.cards), 52)

	def testShuffle(self):
		shuffled = []

		for i in range(0, 100):
			shuffled.append([c.code for c in self.deck.cards])
			self.deck.shuffle()
			self.assertNotIn([c.code for c in self.deck.cards], shuffled)

	def testSortWithoutShuffle(self):
		self.deck.sort()
		self.assertEqual([c.code for c in self.deck.cards], range(0, 52))

	def testSortWithShuffle(self):
		self.deck.shuffle()
		self.deck.sort()
		self.assertEqual([c.code for c in self.deck.cards], range(0, 52))

	def testDrawNumberOfCardsLeft(self):
		self.deck.draw()
		self.assertEqual(len(self.deck.cards), 51)

	def testDrawCardsLeft(self):
		card = self.deck.draw()
		self.assertNotIn(card.code, [c.code for c in self.deck.cards])

class HandTests(unittest.TestCase):
	"""Hand tests"""

	def setUp(self):
		self.hand = Hand(Deck())

	def testNumberOfCards(self):
		self.assertEqual(len(self.hand.cards), 2)

class PlayerTests(unittest.TestCase):
	"""Tests players"""

	def testPlayerName(self):
		p = Player('John')
		self.assertEqual(str(p), 'John')

class DealerTests(unittest.TestCase):
	"""Tests dealers"""

	def setUp(self):
		self.dealer = Dealer('Jane')

	def testDealerName(self):
		self.assertEqual(str(self.dealer), 'Jane')

	def testDealNumberOfPlayers(self):
		deal = self.dealer.deal(Deck(), [Player(), Player()])
		self.assertEqual(len(deal['players']), 2)

	def testDealPlayerNames(self):
		deal = self.dealer.deal(Deck(), [Player('a'), Player('b')])
		self.assertTrue('a' in deal['players'][0] or 'b' in deal['players'][0])
		self.assertTrue('a' in deal['players'][1] or 'b' in deal['players'][1])

	def testDealNumberOnTable(self):
		deal = self.dealer.deal(Deck(), [Player(), Player()])
		self.assertEqual(len(deal['table']), 5)

class GameTests(unittest.TestCase):
	"""Tests games"""

	def setUp(self):
		self.game = Game(Dealer(), [Player(), Player()])

	def testPlayNone(self):
		self.assertEqual(self.game.play(0), [])

	def testPlayDefault(self):
		self.assertEqual(len(self.game.play()), 1)

	def testPlayRandom(self):
		self.assertEqual(len(self.game.play(165)), 165)


def main():
	unittest.main()

if __name__ == '__main__':
	main()