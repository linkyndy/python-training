import random

class Card(object):
	def __init__(self, code):
		self.code = code

	def __str__(self):
		codes = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')
		symbols = (u'\u2660', u'\u2663', u'\u2665', u'\u2666')

		return (codes[self.code%13] + symbols[self.code/13]).encode('utf-8')

class Deck(object):
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
	def __init__(self, deck):
		self.cards = [deck.draw(), deck.draw()]

	def __str__(self):
		return '  '.join([str(card) for card in self.cards])

class Player(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

class Dealer(Player):
	def deal(self, players, times=1):
		deck = Deck()
		game = {}

		for time in range(0, times):
			deck.shuffle()
			game['players'] = [{p: Hand(deck)} for p in players]
			game['table'] = [deck.draw() for i in range(0, 5)]

		return game