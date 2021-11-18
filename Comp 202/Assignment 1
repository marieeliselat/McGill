#Marie-Elise Latorre
#260981320
 
#define global variables
Hearts = 0
Diamonds = 1
Clubs = 2
Spades = 3
 
two = 0
three = 1
four = 2 
five = 3
six = 4
seven = 5
eight = 6
nine = 7
ten = 8
jack = 9
queen = 10
king = 11
ace = 12
 
#what is the suit
def get_suit(card):
    """
    (int) -> int
    Return specififed card's suit as an integer
    
    >>> get_suit(7)
    2
    >>>get_suit(52)
    3
    >>>get_suit(21)
    0
    """
    
    #spades
    a = (card % 4 == 0)
    #hearts
    b = (card % 4 == 1)
    #diamonds
    c = (card % 4 == 2)
    #clubs
    d = (card % 4 == 3)
    
    #if statement to figure out if card = spades or clubs pr diamonds or heart
    if a == True:
        return Spades
    elif d == True:
        return Clubs 
    elif c == True:
        return Diamonds
    elif b == True:
        return Hearts
 
    
def get_rank(card):
    """
    (int) -> int
    Return specified card's rank as an integer
    
    >>> get_rank(7)
    1
    """
    #card -1 means I start from 0
    # so when dividing by 4, get the rank
    return int((card-1)/4)
    
 
def same_rank(card1, card2):
    """
    (int,int) -> bool
    Returns True if both cards are ofthe same rank
    
    >>> same_rank(1,3)
    True
    >>> same_rank(20,3)
    False
    >>> smae_rank(50,52)
    True
    """
    #call get_rank and make both equal with card1 and card2 parameter
    if get_rank(card1) == get_rank(card2):
        return True
    else:
        return False
 
    
def same_suit(card1, card2):
    """
    (int,int) -> bool
    Returns True if both cards are of the same suit
    
    >>>same_suit(7,15)
    True
    >>>same_suit(10,15)
    False
    >>>same_suit(29,1)
    True
    """
    #call get_suit and make it equal to the other one
    if get_suit(card1) == get_suit(card2):
        return True
    else:
        return False
 
     
def same_color_suit(card1, card2):
    """
    (int, int) -> bool
    Returns True if both cards are of the same color of suit
    
    >>>same_color_suit(5,6)
    True
    >>> same_color_suit(1, 2)
    True
    >>>same_color_suit(8, 49)
    False
    
    """
    #red suit
    a = (get_suit(card1) == Hearts)
    b = (get_suit(card1) == Diamonds)
    c = (get_suit(card2) == Hearts)
    d = (get_suit(card2) == Diamonds)
    
    red = (a == b == c == d)
    
    #black suit
    e = (get_suit(card1) == Clubs)
    f = (get_suit(card1) == Spades)
    g = (get_suit(card2) == Clubs)
    h = (get_suit(card2) == Spades)
    
    black = (e == f == g == h)
    
    if red == True:
        return True
    elif black == True:
        return True
    else:
        return False
 
