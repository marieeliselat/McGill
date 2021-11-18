#Marie-Elise Latorre
#260981320

from card2 import *

def draw(hand, top_discard_card):
    """
    (list,int or None) -> str
    Asks the user to enter either 'stock' or 'discard' and returns that string
    >>> import human_player
    >>> location = human_player.draw([4, 50, 15, 21], 5)
    Draw location: stock
    >>> print(location)
    stock
    """
    #variable asking for input
    location = input('Draw location: ')
    
    #return 'stock' if None is given
    if top_discard_card == None:
        return 'stock'
    elif location == 'stock':
        return 'stock'
    else:
        return 'discard'

def discard(hand):
    """
    (list) -> int
    Prints out each card and its index in the list.
    Asks the user to enter one of the indices, and returns the card at that index.
    >>> import human_player
    >>> card_to_discard = human_player.discard([4, 50, 15, 21])
    0 TWO of SPADES
    1 ACE of DIAMONDS
    2 FIVE of CLUBS
    3 SEVEN of HEARTS
    Choice: 2
    >>> print(card_to_discard)
    15
    """
    z = ''
    #print out all the index and name of the card
    for a in hand:
        z = card_to_string(a)
        print(hand.index(a), z, end='\n')
    
    #ask for input
    s = input('Choice: ')
    #convert input into integer
    w = int(s)
    #return the element 
    return hand[s]

    
    
        
    
        

    
    
#Marie-Elise Latorre
#260981320
 
from card2 import *
 
def draw(hand, top_discard_card):
    """
    (list,int or None) -> str
    Asks the user to enter either 'stock' or 'discard' and returns that string
    >>> import human_player
    >>> location = human_player.draw([4, 50, 15, 21], 5) 
    Draw location: stock 
    >>> print(location) 
    stock 
    """
    #variable asking for input
    location = input('Draw location: ')
    
    #return 'stock' if None is given
    if top_discard_card == None:
        return 'stock'
    elif location == 'stock':
        return 'stock'
    else:
        return 'discard'
 
def discard(hand):
    """
    (list) -> int
    Prints out each card and its index in the list.
    Asks the user to enter one of the indices, and returns the card at that index.
    >>> import human_player
    >>> card_to_discard = human_player.discard([4, 50, 15, 21])
    0 TWO of SPADES
    1 ACE of DIAMONDS
    2 FIVE of CLUBS
    3 SEVEN of HEARTS
    Choice: 2
    >>> print(card_to_discard)
    15
    """
    z = ''
    #print out all the index and name of the card
    for a in hand:
        z = card_to_string(a)
        print(hand.index(a), z, end='\n')
    
    #ask for input
    s = input('Choice: ')
    #convert input into integer
    w = int(s)
    #return the element 
    return hand[s]
