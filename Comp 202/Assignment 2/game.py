#Marie-Elise Latorre
#260981320
from card2 import *
def calculate_winner(points):
    """
    (list) -> list
    Returns a list containing the indices of the list corresponding to the lowest points in the points list
    >>> calculate_winner([100, 5, 20, 42]) 
    [1] 
    >>> calculate_winner([100, 5, 20, 5]) 
    [1, 3] 
    """
    N = []
    r=['','','','','','','','','','','']
    a = (min(points))#minimum number of the list
    for index in range(len(points)):
        if points[index] == a: # check if the minimum number is the current element in the for loop
            N.append(((points.index((points[index]))))) #append it to N
            points[index]=r[index] #switch the minimum number to an empty string,
                                   #so that when the for loop goes again, it doesn't count the index again
    return N
 
 
 
def calculate_round_points(hand):
    """
    (list) -> int
    Returns the point value of that hand
    >>> calculate_round_points([1, 2, 3, 4])
    8
    >>> calculate_round_points([49, 50, 51, 52])
    4
    """
    
    a = 0
    
    for y in hand:
        if y in range(1,5): #2s 
            a += 2 
        elif y in range(5,9):#3s 
            a += 3 
        elif y in range(9,13):#4s 
            a += 4 
        elif y in range(13,17): #5s 
            a += 5 
        elif y in range(17,21):#6s 
            a += 6 
        elif y in range(21,25):#7s 
            a += 7 
        elif y in range(25,29):#8s 
            a += 8 
        elif y in range(29,33):#9s 
            a += 9 
        elif y in range(33,49):#Cards of 10s, Jack, King, Queen 
            a += 10 
        elif y in range(49,53):#ACE 
            a += 1 
            
    return a
        
 
def is_valid_group(cards):
    """
    (list) -> bool
    Returns True if the cards form a valid group, and False otherwise
    >>> is_valid_group([1, 2, 3])
    True
    >>> is_valid_group([1, 2, 3, 52])
    False
    """
    for u in range(len(cards)):
        if (((cards[u]) // 4)) == (((cards[-1])//4)): #see if the two cards are in the same group
            if (((cards[u]) // 4)) == (((cards[u+1])//4)):
                return True 
        return False
   
 
def is_valid_sequence(cards):
    """
    (list) -> bool
    Returns True if the cards form a valid sequence, and False otherwise
    >>> is_valid_sequence([1, 5, 9])
    True
    >>> is_valid_sequence([1, 5, 10])
    False
    >>> is_valid_sequence([30, 34])
    False
    >>> is_valid_sequence([34, 38, 30])
    True
    """
    #check if there are at least 3 elements in the list
    if len(cards) >= 3:
        for w in range(len(cards)): 
            if str((cards[w])/4)[1:] == str((cards[-1])/4)[1:]: #is the first element in the sequence as the last one
                if (cards[w]) != (cards[-1]): #make sure to not get out of range error
                  if int((cards[w]//13)) == int((cards[w+1]//13)): #is the next element also in the sequence
                     return True
                return True
            return False
 
    return False
