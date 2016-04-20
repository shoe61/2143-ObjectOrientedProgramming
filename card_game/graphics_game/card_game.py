from graphics import *
import os
import random


"""
This website gave me the asii idea. 
http://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards
"""

"""
@Class AsciiCard 
@Description:
    This class reads 53 (52 cards, and 1 back) ascii representations of a deck of cards from the given file.
@method get_ascii(string,int)
"""
class GameCardImage(object):

    suits = ['spades','hearts','diamonds','clubs']
    card_images = []
    
    def __init__(self,cards_dir="./card_images/xsmall/",back='back_red.gif'):
        self.path = cards_dir
        self.card_back = back
        for filename in os.listdir(self.path):
            self.card_images.append(self.path+filename)

    """
    @Description:
        This method takes a card suit, and an integer between 2,14 inclusive and 
        returns the correpsoning ascii representation of that card. 
    @Example:
    """
    def get_image(self,suit=None,rank=None):
        if suit == None or rank == None:
            return self.path + self.card_back;
            
        if type(suit) is str:
            suit = self.suits.index(suit)
        return self.card_images[((suit * 13) + rank) - 1] ;
            
        
        
"""
@Class Card 
@Description:
    
"""
class Card(GameCardImage):
    ranks = [None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]

    def __init__(self, suit='', rank=0):
        super().__init__()
        
        # If user passes in an int between 0-3, then convert it to string
        # otherwise keep the string 
        if type(suit) is int:
            self.suit = self.suits[suit]
        else:
            self.suit = suit
            
        self.rank = rank
        self.card_image = self.get_image(self.suit,self.rank)

    def __str__(self):
        return (self.card)
           
    def __cmp__(self,other):
        t1 = self.suit,self.rank
        t2 = other.suit,other.rank
        return int(t1[1])<int(t2[1])
   
    # Python3 wasn't liking the __cmp__ to sort the cards, so 
    # documentation told me to use the __lt__ (less than) 
    # method.
    def __lt__(self,other):
        return self.__cmp__(other)
        
"""
@Class Deck 
@Description:
    This class represents a deck of cards. 
@Methods:
    pop_cards() - removes a card from top of deck
    add_card(card) - adds a card to bottom of deck
    shuffle() - shuffles deck
    sort() - sorts the deck based on value, not suit (could probaly be improved based on need)
"""       
class Deck(object):
    def __init__(self):
        #assume top of deck = 0th element
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit,rank))
                
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return " ".join(res)
    
    def pop_card(self):
        return self.cards.pop(0)
        
    def add_card(self,card):
        self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards = sorted(self.cards)
       
"""
@Class: Hand 
@Extends: Deck
@Description:
    This class represents a hand of cards 
@Methods:
""" 
class Hand(Deck):
    def __init__(self,label=''):
        self.cards = []
        self.label = label
        
        
def main():
    win = GraphWin("My Circle", 800, 300)
    
    hand = Hand()
    hand.add_card(Card(2,13))
    hand.add_card(Card(2,11))
    hand.add_card(Card(2,9))
    hand.add_card(Card(2,10))
    hand.add_card(Card(2,8))
    
    images = []

    x = 100
    y = 100
    for c in hand.cards:
        print(c.card_image)
        images.append(Image(Point(x,y),c.card_image))
    #     x+= 150
    # for i in images:
    #     i.draw(win)
        

    win.getMouse() # Pause to view result
    win.close()    # Close window when done    
        
if __name__=='__main__':

    g = GameCardImage()
    print(g.get_image(2,13))
    main()