import random

class Card(object):
	"""Handles individual cards"""

	def __init__(self, code):
		self.code = code

	def __str__(self):
		codes = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')
		symbols = (u'\u2660', u'\u2663', u'\u2665', u'\u2666')

		return (codes[self.code%13] + symbols[self.code/13]).encode('utf-8')

class Deck(object):
	"""Handles a deck consisting of 52 cards"""

	def __init__(self):
		self.cards = [Card(i) for i in range(0, 52)]

	def __str__(self):
		return '  '.join([str(card) for card in self.cards])

	def shuffle(self):
		random.shuffle(self.cards)

	def sort(self):
		self.cards.sort()

	def draw(self):
		return self.cards.pop()

class Hand(object):
	"""Handles a hand consisting of 2 cards"""

	def __init__(self, deck):
		self.cards = [deck.draw(), deck.draw()]

	def __str__(self):
		return '  '.join([str(card) for card in self.cards])

class Player(object):
	"""Handles players involved in the game"""

	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

class Dealer(Player):
	"""Handles the dealer of the game"""

	def deal(self, players):
		"""Creates a deck and deals the cards to the players
		and on the table
		"""

		deck = Deck()
		
		return {
			'players': [{p: Hand(deck)} for p in players], 
			'table': [deck.draw() for i in range(0, 5)]
		}

class Game(object):
	"""Handles the poker game itself"""

	def __init__(self, dealer, players, deal_times=1):
		self.dealer = Dealer(dealer)
		self.players = players
		self.deal_times = deal_times

	def play(self):
		"""Plays a game consisting of several deal times"""
		
		game = []

		for time in range(0, self.deal_times):
			game.append(self.dealer.deal(self.players))

		return game