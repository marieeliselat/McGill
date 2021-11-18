#Marie-Elise Latorre
#260981320
 
from vectors_utils import *
from math import *
 
def get_semantic_descriptor(w, s):
    '''
    (str, list) -> dict
    returns a dictionary representing the semantic descriptor vector of the
    word w computed from the sentence s
    >>> s1 = ['all', 'the', 'habits', 'of', 'man', 'are', 'evil']
    >>> s2 = ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal']
    >>> desc1 = get_semantic_descriptor('evil', s1)
    >>> desc1['all']
    1
    >>> len(desc1)
    6
    >>> 'animal' in desc1
    False
    >>> desc2 = get_semantic_descriptor('animal', s2)
    >>> desc2 == {'no': 1, 'must': 1, 'ever': 1, 'kill': 1, 'any': 1, 'other': 1}
    True
    >>> get_semantic_descriptor('animal', s1)
    {}
    '''
    
    d = {}
    
    if w not in s: #if word not in string return empty dict
        return d
    else:
        for i in s:#itrate through the list
            if (i == w): #if the element is the same as the string , pass it
                continue
            elif i in d: #if the element is already in d add 1
                d[i] += 1
            else: #if not then it's equal to one
                d[i] = 1
    return d  
 
 
 
def get_all_semantic_descriptors(sim):
    '''
    (list) -> dict
    Returns a dictionary d such that for every word w that appears
    in at least one of the sentences, d[w] is itself a dictionary
    which represents the semantic descriptor vector of w
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> d = get_all_semantic_descriptors(s)
    >>> d['animal']['must']
    3
    >>> d['evil'] == {'all': 1, 'the': 1, 'habits': 1, 'of': 1, 'man': 1, 'are': 1}
    True
    >>> get_all_semantic_descriptors([['I', 'live', 'on', 'the', 'road'], ['and', 'yeah']]))
    {'I': {'live': 1, 'on': 1, 'the': 1, 'road': 1}, 'live': {'I': 1, 'on': 1, 'the': 1, 'road': 1},
    'on': {'I': 1, 'live': 1, 'the': 1, 'road': 1}, 'the': {'I': 1, 'live': 1, 'on': 1, 'road': 1},
    'road': {'I': 1, 'live': 1, 'on': 1, 'the': 1}, 'and': {'yeah': 1}, 'yeah': {'and': 1}}
    >>> get_all_semantic_descriptors(['yeh']))
    {'y': {'e': 1, 'h': 1}, 'e': {'y': 1, 'h': 1}, 'h': {'y': 1, 'e': 1}}
    '''
    d = {}
    for i in sim: #iterate through the list
        for e in i: #iterate through the words
            if e not in d: #if the word is not in d, get it's semantic descriptor
                d[e] = get_semantic_descriptor(e, i)
            else:
                add_vectors(d[e], get_semantic_descriptor(e,i))
    return d
 
def get_cos_sim(vec1, vec2):
    '''
    (dict, dict) -> float
    Returns the cosine similarity between the two dictionaries
    >>> round(get_cos_sim({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}), 2)
    0.7
    
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> d = get_all_semantic_descriptors(s)
    >>> v1 = d['evil']
    >>> v2 = d['animal']
    >>> round(get_cos_sim(v1, v2), 4)
    0.0595
    
    >>> w = [['i'], ['live', 'on', 'the', 'road']]
    >>> r = get_all_semantic_descriptors(w)
    >>> vec1 = r['i']
    >>> vec2 = r['on']
    >>> get_cos_sim(vec1, vec2)
    0.0
    
    >>> w = [['i'], ['yeh']]
    >>> r = get_all_semantic_descriptors(w)
    >>> vec1 = r['i']
    >>> vec2 = r['yeh']
    >>> get_cos_sim(vec1, vec2)
    0.0
    '''
    try:
        cosine_similarity = get_dot_product(vec1, vec2) / (get_vector_norm(vec1) * get_vector_norm(vec2))
    except ZeroDivisionError: #catch ZeroDivisionError
        return 0.0
    return cosine_similarity
 
def get_euc_sim(vec1, vec2):
    '''
    (dict, dict) -> float
    Returns the similarity between the two using the negative euclidean distance
    >>> round(get_euc_sim({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}), 2)
    -6.71
    
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> d = get_all_semantic_descriptors(s)
    >>> v1 = d['evil']
    >>> v2 = d['animal']
    >>> round(get_euc_sim(v1, v2), 4)
    -7.1414
    
    >>> w = [['i'], ['live', 'on', 'the', 'road']]
    >>> r = get_all_semantic_descriptors(w)
    >>> vec1 = r['i']
    >>> vec2 = r['on']
    >>> get_euc_sim(vec1, vec2)
    -1.7320508075688772
    
    >>> w = [['i'], ['yeh']]
    >>> r = get_all_semantic_descriptors(w)
    >>> vec1 = r['i']
    >>> vec2 = r['yeh']
    >>> get_euc_sim(vec1, vec2)
    -0.0
    
    '''
    vec1_minus_vec2 = sub_vectors(vec1, vec2) #use function from vectors_utils
    return - (get_vector_norm(vec1_minus_vec2)) #do the equation
    
def get_norm_euc_sim(vec_1, vec_2):
    '''
    (dict, dict) -> float
    Returns the similarity between the two using the
    negative euclidean distance between the normalized vectors
    >>> round(get_norm_euc_sim({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}), 2)
    -0.77
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> d = get_all_semantic_descriptors(s)
    >>> v1 = d['evil']
    >>> v2 = d['animal']
    >>> round(get_norm_euc_sim(v1, v2), 4)
    -1.3715
    
    >>> w = [['i'], ['live', 'on', 'the', 'road']]
    >>> r = get_all_semantic_descriptors(w)
    >>> vec1 = r['i']
    >>> vec2 = r['on']
    >>> get_norm_euc_sim(vec1, vec2)
    -1.0
    
    '''
    
    normalize_vector(vec_1) 
    
    normalize_vector(vec_2)
    
    return get_euc_sim(vec_1, vec_2) #get_euc_sim of the normalized vetors 
