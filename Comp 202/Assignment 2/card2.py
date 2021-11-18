#Marie-Elise Latorre
#260981320
 
from card1 import * 
SUITS = [0, 1, 2, 3]
RANKS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
SUITS_STR = ['HEARTS', 'DIAMONDS', 'CLUBS', 'SPADES']
RANKS_STR = ['TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING', 'ACE']
 
def get_card(suit,rank):
    """
    (int,int) -> int
    Returns the integer representation of the card with that suit and rank
    
    >>>get_card(HEARTS, TWO)
    1
    >>>get_card(HEARTS, THREE)
    5
    >>>get_card(3, 12)
    52
    """
    # inverse of get_rank and get_suit
    r = (rank)*4
    s = (SUITS.index(suit)) 
    return r+1+s
 
def card_to_string(card):
    """
    (int) -> str
    Returns a string for that card's name in the form RANK of SUIT
    >>>card_to_string(1)
    'TWO of HEARTS'
    >>>card_to_string(5)
    'THREE of HEARTS'
    >>>card_to_string(52)
    'ACE of SPADES'
    """
    #local variables
    r = get_rank(card)
    s = (get_suit(card))
    
    #get rank of card
    for i in range(len(RANKS)) : 
        if RANKS[i] == r:  
            d = RANKS_STR[i]  
             
    #get suit of card  
    for h in range(len( SUITS)) : 
        if SUITS[h] == s: 
            a = SUITS_STR[h] 
      
    #concatenate everything together  
    y=' of '    
    return d+y+a
 
 
def hand_to_string(hand):
    """
    (list) -> str
    Returns a string containing the names of all the cards, each card name being separated by a comma and a space.
    >>>hand_to_string([1, 2, 3, 4]) 
    'TWO of HEARTS, TWO of DIAMONDS, TWO of CLUBS, TWO of SPADES' 
    >>> hand_to_string([52]) 
    'ACE of SPADES' 
    """
    p = ''
    
    for e in hand:
        p += card_to_string(e) #transform the numbers in the list into string
        if len(hand) > 1: #if there are more elements add a comma
            if hand[e-1] != hand[-1]:
                p += ', '
        else:
            p+=''  
    return p
 
 
    
def get_deck():
    """
    (void) -> list
    Returns a list of integers containing the 52 cards
    in a deck of playing cards (one card of each suit and rank).
    
    >>> deck = get_deck()
    >>> len(deck)
    52
    """
 
    deck =[]
    #append 52 numbers in a list
    for i in range(1,53):
        deck.append(i)
    return deck
        
 
 
 
    
def all_same_suit(cards):
    """
    (list) -> bool
    Returns True if all cards in the list are of the same suit, and False otherwise.
    >>>all_same_suit([4, 52])
    True
    >>> all_same_suit([1, 2, 3, 4])
    False
    """
    
    for q in range(len(cards)):
        if same_suit(cards[q], cards[-1]): #check if the suit is the same
            if cards[q] != cards[-1]: #don't get the out of range error
                if same_suit(cards[q],cards[q+1]): #check if the next card is also in the same suit
                    return True
            return True
        else:
            return False
 
 
 
def all_same_rank(cards):
    """
    (list) -> bool
    Returns True if all cards in the list are of the same rank, and False otherwise.
    >>> all_same_rank([4, 52])
    False
    >>> all_same_rank([1, 2, 3, 4])
    True
    """
    for h in range(len(cards)):
        if same_rank(cards[h], cards[-1]):#check if the rank is the same
            if cards[h] != cards[-1]: #don't get the out of range error
                if same_suit(cards[h],cards[h+1]): #check if the next card is also in the same rank
                    return True
            return True
        else:
            return False
