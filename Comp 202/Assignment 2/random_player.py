#Marie-Elise Latorre
#260981320
 
import random
 
def draw(hand, top_discard_card):
    """
    (list,int or None) -> str
    Returns either 'stock' or 'discard' at random (unless there is no top card in the discard pile,
    in which case only 'stock' should be returned).
    >>> import random_player
    >>> random_player.draw([4, 50, 15, 21], 5)
    'stock' #or 'discard', randomly
    >>> random_player.draw([4, 50, 15, 21], None)
    'stock'
    """
    #random stock or discard
    
    choice = ['stock', 'discard']
    
        
    #check if None to return stock
    if top_discard_card == None:
        return 'stock'
    return choice[random.randint(0,1)]
    
 
    
    
    
def discard(hand):
    """
    (list) -> int
    Returns a random card in the hand
    >>> import random_player
    >>> random_player.discard([4, 50, 15, 21])
    50 # or 4, 15, or 21
    
    """
    
    #between 0 and the length of the hand -1 choose  random number --> index
    #return the number at the index of it
    return hand[random.randint(0,len(hand)-1)]
