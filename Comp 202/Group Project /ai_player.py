#Marie-Elise Latorre - 260981320 
#Sherry Shang - 260919055
#Diego A. Contreras - 260965809
#James Moore - 260942322
from arrangement import *
 
def makes_best_arrangement(the_arrangement, your_int):
    '''
    (list, int) -> Bool
    
    this is a helper function which looks inside a nested list to determine if the given int is inside it
    
    >>> makes_best_arrangement([[1,2,3],[4,5,6]], 6)
    True
    >>> makes_best_arrangement([[1]],1)
    True
    >>> makes_best_arrangement([[1,2,3],[4,5,6]],7)
    False
    '''
    for i in the_arrangement:
        if your_int in i:
            return True
    return False
 
def draw(hand, top_discard, last_turn, picked_up_discard_cards, player_position, wildcard_rank, num_turns_this_round):
    '''
    (list, int or None, bool, list, list, int, int) -> str
    
    From instruction: "This function decides from where to pick up a card: from the discard pile or from the stock."
    The decision can be made based on any number of the given arguments.
    
    >>> draw([1,42,30,51], None, False, [[],[],[],[]], 0, 0, 0)
    'stock'
    >>> draw([1,2,3,51], 4, False, [[1],[5],[7],[47,33]], 0, 0, 6)
    'discard'
    >>> draw([1,2,3,51], 5, False, [[1],[6],[7],[47,33]], 0, 1, 6)
    'discard'
    >>> draw([1,2,3,51], 28, False, [[7,10,13],[6,9,52],[1,3],[25,26,27]], 2, 0, 11)
    'discard'
    '''
    # the following is a sequence of conditionals placed in order of importance:
    if top_discard == None: 
        return 'stock'
    else:
        #makes copy of hand list in order to avoid changing original list:
        possible_arrangement = hand[:] + [top_discard] 
        #creates best arrangement from hand + top_discard:
        possible_arrangement2 = get_arrangement(tuple(possible_arrangement), wildcard_rank)
        if makes_best_arrangement(possible_arrangement2, top_discard):
            return 'discard'
        if get_rank(top_discard) == wildcard_rank:
            return 'discard'
        next_player_index = player_position + 1
        #in order to avoid any index errors:
        if next_player_index >= len(picked_up_discard_cards):
            next_players_picked_up_cards = picked_up_discard_cards[0]
        else:
            next_players_picked_up_cards = picked_up_discard_cards[next_player_index]
        #similar process as above, using the next player's picked up cards + top_discard as their hand:
        next_players_arrangement = next_players_picked_up_cards[:] + [top_discard]
        next_players_arrangement2 = get_arrangement(tuple(next_players_arrangement), wildcard_rank)
        if makes_best_arrangement(next_players_arrangement2, top_discard):
            return 'discard'
        else:
            return 'stock'
 
def discard(hand, last_turn, picked_up_discard_cards, player_index, wildcard_rank, num_turns_this_round):
    '''
    (list, bool, list, int, int,int) -> str
    
    Returns which card to discard
    
    >>> discard([1,1,2,7], True, [[1,2],[3,4]],2,3,4))
    7
    >>> discard([1,1,2,21], False, [[1,2],[3,4]],2,3,4))
    21
    >>>discard([1,1,2,21], False, [[1]],[3,4,5,7,9]],2,3,4))
    21
    >>>discard([1,1,2,20,6,49], False, [[1],[3,4,5,7,9]],2,3,4))
    20
    >>>discard([1,1,2,52,20,6], True, [[1],[3,4,5,7,9]],0,9,0)
    52
    >>>discard([1,1,2], False, [[1],[3,4,5,7,9]],1,3,3)
    2
    '''
    list1=[]
    # get the best arrangement for hand
    best_arrangement=get_arrangement(tuple(hand), wildcard_rank)
    # putting all cards in best arrangement into a new list 
    for combination in best_arrangement:
        for element in combination:
            list1.append(element)
    # Find a list of cards which not in the best arrangement
    discard_card=[]
    for element in hand: 
        if element not in list1:
            discard_card.append(element)
    # If a wildcard in the discard_card then don't discard them
    m=discard_card[:]
    for element in discard_card:
        if get_rank(element) == wildcard_rank:
            discard_card.remove(element)
    #remove highest penalty cards
    if last_turn == True:
        for i in discard_card: 
            if 12 == get_rank(i): #check if it's an ACE card
                i = 0 #make it the lowest number card
        return (max(discard_card)) #discard the highest penalty card, thus the largest card
        
    #if a combination is almost finished, we don’t discard those
    x=[]
    y=[]
    if len(discard_card)>1: # if there is only one card other than wildcard
        for i in range(len(discard_card)): 
            a=get_rank(discard_card[i])
            b=get_suit(discard_card[i])
            for m in range(len(discard_card)): # check if there is a almost group(two cards with same rank)
                if m!=i and get_rank(discard_card[m])==a:
                    if discard_card[m]not in x and discard_card[i]not in x:
                        x.append(discard_card[m])
                        x.append(discard_card[i])
                elif m!=i and get_suit(discard_card[m])==b and abs(a-get_rank(discard_card[m]))<3: #check if there is a almost sequence
                    if discard_card[m] not in y and discard_card[i]not in y:
                        y.append(discard_card[m])
                        y.append(discard_card[i])
        for element in x+y: # remove the card from discard_card if it's part of a almost combination
            if element in discard_card:
                discard_card.remove(element)
        if discard_card==[]: # if all cards are removed from discard_card
            z=x+y
        elif discard_card!=[]:
            z=discard_card
        # checking points of each cards
        point=[2,3,4,5,6,7,8,9,10,10,10,10,1]
        w=[]
        final_discard=[]
        for element in z:
            w.append(point[get_rank(element)])
            max_point=max(w) # checking for the largest point
        for i in range(len(w)): # if cards in z has the largest point, then add to final_discard
            if w[i] == max_point:
                final_discard.append(z[i])
        return final_discard[0] 
    else:
        for i in hand: 
            if 12 == get_rank(i): #check if it's an ACE card
                i = 0 #make it the loweest number card
            return (max(hand))
