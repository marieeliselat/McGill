#Marie-Elise Latorre
#260981320
 
import math
 
def add_vectors(v1, v2):
    '''
    (vec, vec) -> void
    Adds the second vector to the first one
    >>> v1 = {'a' : 1, 'b' : 3}
    >>> v2 = {'a' : 1, 'c' : 1}
    >>> add_vectors(v1, v2)
    >>> len(v1)
    3
    >>> v1['a']
    2
    >>> v1 == {'a' : 2, 'b' : 3, 'c' : 1}
    True
    >>> v2 == {'a' : 1, 'c' : 1}
    True
    >>> vector_1 = {'z' : 1, 'y' : 3}
    >>> vector_2 = {'u' : 4, 'z' : 1, 'p': 12}
    >>> add_vectors(vector_1, vector_2)
    >>> print(vector_1)
    {'z': 2, 'y': 3, 'u': 4, 'p':12}
    >>>add_vectors(vector_2, vector_1)
    >>>print(vector_1)
    {'z': 1, 'y':3}
    
    '''
    for i in v2.keys(): #iterate through each key in v2
        if i in v1.keys(): #check if those keys are in v1
            v1[i] = v2.get(i) + v1.get(i) #if yes add their values
        else:
            v1[i] = v2.get(i) #if not simply store in v1
 
def sub_vectors(d1, d2):
    '''
    (vec, vec) -> vec
    Returns a  dictionary which is the result
    of subtracting the second vector from the first one
    >>> d1 = {'a' : 3, 'b': 2}
    >>> d2 = {'a': 2, 'c': 1, 'b': 2}
    >>> d = sub_vectors(d1, d2)
    >>> d == {'a': 1, 'c' : -1}
    True
    >>> d1 == {'a' : 3, 'b': 2}
    True
    >>> d2 == {'a': 2, 'c': 1, 'b': 2}
    True
    >>> vector_1 = {'z' : 1, 'y' : 3}
    >>> vector_2 = {'u' : 4, 'z' : 1, 'p': 12}
    >>> print(sub_vectors(vector_2, vector_1))
    {'u': 4, 'p': 12, 'y': -3}
    >>> sub_vectors(vector_1, vector_2)
    {'y': 3, 'u': -4, 'p': -12}
    '''
    dict_1 = {}
    dict_2 = {}
     
    #copy d1 to dict_1 (to avoid making changes)
    for i in d1:
        dict_1[i] = d1[i]
    
    #do the same for d2
    for i in d2:
        dict_2[i] = d2[i]
    
    #make no values equal to 0
    for i in dict_1:
        if i not in dict_2:
            dict_2[i] = 0
            
    #same for dict_2
    for i in dict_2:
        if i not in dict_1:
            dict_1[i] = 0
            
    #store result in new variable
    result = {}
    
    #subtract and get rid of 0 (we don't need to store them)
    for i in dict_1:
        r = dict_1[i] - dict_2[i]
        if r != 0:
            result[i] = r
            
    return result
 
def merge_dicts_of_vectors(d1, d2):
    '''
    (vec, vec) -> void
    Modifies the first input by merging it with the second one
    >>> d1 = {'a' : {'apple': 2}, 'p' : {'pear': 1, 'plum': 3}}
    >>> d2 = {'p' : {'papaya' : 6}}
    >>> merge_dicts_of_vectors(d1, d2)
    >>> len(d1)
    2
    >>> len(d1['p'])
    3
    >>> d1['a'] == {'apple': 2}
    True
    >>> d1['p'] == {'pear': 1, 'plum': 3, 'papaya' : 6}
    True
    >>> d2 == {'p' : {'papaya' : 6}}
    True
    
    >>> merge_dicts_of_vectors(d2, d1)
    >>> d2['a']['apple']
    2
    >>> d2['p']['papaya']
    12
    
    >>> vector1 = {'e' : {'easle': 0}, 'i' : {'igloo': 1, 'idiot': 3}}
    >>> vector2 = {'w' : {'willies' : 200}, 'l' : {'lmao': 42}}
    >>> merge_dicts_of_vectors(vector1, vector2)
    >>> print(vector1)
    {'e': {'easle': 0}, 'i': {'igloo': 1, 'idiot': 3}, 'w': {'willies': 200}, 'l': {'lmao': 42}}
    '''
    #check for keys
    for key in d2:
        if key in d1: 
            for i in d2[key]: #update the dict 
                if i in d1[key]:
                    d1[key][i] += d2[key][i] 
                else:
                    d1[key][i] = d2[key][i]
        else: #add the keys in the first dict
            d1[key] = d2[key]
 
def get_dot_product(v1, v2):
    '''
    (vec, vec) -> vec
    Returns the dot product of the two vectors
    >>> v1 = {'a' : 3, 'b': 2}
    >>> v2 = {'a': 2, 'c': 1, 'b': 2}
    >>> get_dot_product(v1, v2)
    10
    >>> v3 = {'a' : 3, 'b': 2}
    >>> v4 = {'c': 1}
    >>> get_dot_product(v3, v4)
    0
    >>> vector1 = {'e' : {'easle': 0}, 'i' : {'igloo': 1, 'idiot': 3}}
    >>> vector2 = {'w' : {'willies' : 200}, 'l' : {'lmao': 42}}
    >>> get_dot_product(vector2, vector1)
    0
    '''
    
    dot_product = 0
    
    for i in v1.keys(): 
        if i in v2: #if the keys of dict v1 are in in v2
            dot_product = dot_product + v1[i] * v2[i] #multiply them and add them
                                                      #to dot_product
    return dot_product
 
def get_vector_norm(vec):
    '''
    (vec) -> float
    Returns the norm of such vector
    >>> v1 = {'a' : 3, 'b': 4}
    >>> get_vector_norm(v1)
    5.0
    >>> v2 = {'a': 2, 'c': 3, 'b': 2}
    >>> round(get_vector_norm(v2), 3)
    4.123
    >>> vector1 = {'z' : 0, 'y' : 30120}
    >>> get_vector_norm(vector1)
    30120.0
    '''
    sum_of_squares = 0.0  # floating point to handle large numbers
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)
 
def normalize_vector(vec1):
    '''
    (vec) -> void
    Modifies the dictionary by dividing each value by the norm of the vector
    >>> v1 = {'a' : 3, 'b': 4}
    >>> normalize_vector(v1)
    >>> v1['a']
    0.6
    >>> v1['b']
    0.8
    >>> v2 = {'a': 2, 'c': 3, 'b': 2}
    >>> normalize_vector(v2)
    >>> round(v2['c'], 3)
    0.728
    >>> vector1 = {'z' : 0, 'y' : 30120}
    >>> normalize_vector(vector1)
    >>> print(vector1)
    {'z': 0.0, 'y': 1.0}
    '''
    norm_value = get_vector_norm(vec1)
    for key in vec1:
        vec1[key] /= norm_value
    
