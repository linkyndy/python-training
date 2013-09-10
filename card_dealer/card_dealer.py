class Card(object):
	def __init__(self, code):
		self.code = code

	def __str__(self):
		codes = {0: '2', 1: '3', 12: 'A'}

		return codes[self.code % 13] + ' ' + self.code / 13

class Deck(object):
	def __init__(self):
		self.cards = [Card(i) for i in range(1, )]

	def draw(self):
		pass

class Hand(object):
	def __init__(self):
		pass

class Player(object):
	def __init__(self, name):
		self.name = name

class Dealer(Player):
	def deal(self, players):
		self.players = players

if __name__ == '__main__':
	pass