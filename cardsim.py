#By Jordan Jolo
#May 11 2020 
#PROJECT 5
#I have worked aloneimport random

class Card():

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

#returns what suit the card isreturns what suit the card is#returns what suit the card isreturns what suit the card is
    def getSuit(self): 
        return self.suit

#returns what rank the card isreturns what rank the card is#returns what rank the card isreturns what rank the card is
    def getRank(self): 
        return self.rank

#contain a collection of the 52 instances of Card objects that will be created for the standard deck
class Deck():
    suit = ['SPADES', 'HEARTS', 'CLUBS', 'DIAMONDS']
    rank = [ '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K','A']
    

    def __init__(self):
        self.cards = []
        for rank in Deck.rank:
            for suit in Deck.suit:
                card = Card(rank, suit)
                self.cards.append(card)

#rearrange the order of the cards randomly
    def shuffle(self):
        random.shuffle(self.cards)

#return the "top" card of the deck; if empty, returns None
    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
    

#construct 52 instances of Card matching a standard deck of cards
def main():
    deck = Deck()
    deck.shuffle()
    for i in range(52): 
        card = deck.draw()
        print(card.getRank() +" OF "+ card.getSuit())
main()
