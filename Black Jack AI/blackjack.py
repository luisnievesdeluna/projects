
import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = { 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9,  'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
options = ['H', 'S'] # H = Hit, S = Stand


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit

    def __repr__(self):
        return self.__str__()
    
class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def __str__(self):
        current_deck = '' # set the deck comp as an empty string
        for card in self.deck:
            current_deck += '\n'+ card.__str__() # Card class string representation
        return "The deck has: " + current_deck
                
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        singleCard = self.deck.pop()
        return singleCard

    
class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def card_add(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        
        if card.rank == "Ace":
            self.aces += 1

class Player:
    def __init__(self, genome):
        self.genome = genome

    def playHand(self, hand, dealerCard):
        x = hand.value
        y = dealerCard.value
        c0, c1, c2, c3, c4, c5 = self.genome
        R = c0 + c1*x + c2*y + c3*x**2 + c4*y**2 + c5*x*y
        if R < 0: 
            return 'H'
        else: 
            return 'S'
    

    def playRandom(self, hand):
        if random() < 0.5:
            return 'H'
        else:
            return 'S'


class Game:

    def playSingleHand(self, deck, player):

        playerHand = Hand() # The hand of the player
        dealerHand = Hand() # The hand of the dealer

        playerHand.card_add(deck.deal()) # Deal player first card
        dealerHand.card_add(deck.deal()) # Deal dealer first card
        playerHand.card_add(deck.deal()) # Deal player second card
        dealerHand.card_add(deck.deal()) # Deal dealer second card

        #tests for immediate blackjack
        if playerHand.value == 21: 
            if dealerHand.value == 21:
                return 0
            return 1.5

        if dealerHand.value == 21:
            return -1
        
        #deals to player until they choose to stand
        while player.playHand(playerHand, dealerHand.cards[0]) != 'S':
            playerHand.card_add(deck.deal())
            if playerHand.value > 21: 
                return -1

        #deals to dealer until their cards are valued at 17 or above 
        while dealerHand.value < 17:
            dealerHand.card_add(deck.deal())
            if dealerHand.value > 21: 
                return 1
            elif playerHand.value == 21:
                return 1.5
            
        #returns winnings
        if playerHand.value > dealerHand.value:
            return 1
        elif playerHand.value == dealerHand.value:
            return 0
        return -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        