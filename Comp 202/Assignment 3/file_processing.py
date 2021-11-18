#Marie-Elise Latorre
#260981320
 
from vectors_utils import *
from similarity_measures import *
 
def get_sentences(sentences):
    '''
    (str) -> list
    Returns a list of strings each representing
    one of the sentences from the input string
    
    >>> text = "No animal must ever kill any other animal. All animals are equal."
    >>> get_sentences(text)
    ['No animal must ever kill any other animal', 'All animals are equal']
    >>> t = "Are you insane? Of course I want to leave the Dursleys! Have you got a house? When can I move in?"
    >>> get_sentences(t)
    ['Are you insane', 'Of course I want to leave the Dursleys', 'Have you got a house', 'When can I move in']
    
    >>> i = 'I. dont. Like. BIG. PROblem!????!!!!!'
    >>> get_sentences(i)
    ['I', 'dont', 'Like', 'BIG', 'PROblem']
    
    >>> p = '?!!?. ?ameIcan. dream'
    >>> get_sentences(p)
    ['ameIcan', 'dream']
    '''
    punctuation=[".", "!", "?"]
    sentences = sentences.replace("!", ".")#replace ! with .
    sentences = sentences.replace("?", ".")#replace ? with .
    
    sentences = sentences.split(".") #split it
    temporary_list = []
    for i in sentences:#iterate through the str
        i = i.replace('\n','').strip()#replace new line with empty string and strip it
        if i != '': #get rid of the empty string 
            temporary_list.append(i) #append whatever is left
    
            
    return temporary_list
 
def get_word_breakdown(y):
    '''
    (str) -> list
    Returns a 2D lists of strings
    >>> text = "All the habits of Man are evil. And, above all, no animal must ever tyrannise over his \
    own kind. Weak or strong, clever or simple, we are all brothers. No animal must ever kill \
    any other animal. All animals are equal."
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> w = get_word_breakdown(text)
    >>> s == w
    True
    
    >>> i = 'I. dont. Like. BIG. PROblem!????!!!!!'
    >>> get_word_breakdown(i)
    [['i'], ['dont'], ['like'], ['big'], ['problem']]
    
    >>> p = '?!!?. lo -- ving ::: t;; h -e.  ?ameIcan. dream'
    >>> get_word_breakdown(p)
    [['lo', 'ving', 't', 'h', 'e'], ['ameican'], ['dream']]
    '''
    punctuation = [',', '-', '--', ':', ';', '"', "'"]
    word_breakdown = []
    for punc in punctuation: #get rid of punctuation by replacing it with empty string
        y = y.replace(punc, "")
    sentence_list = get_sentences(y)
    
    for counter,sentence in enumerate(sentence_list): 
        sentence_list[counter] = sentence.lower().split() #for each word in sentence_list, lower it and split 
        
 
    return sentence_list
 
 
def build_semantic_descriptors_from_files(files):
    '''
    (list) -> dict
    Returns a dictionary of the semantic descriptors of all the words in the
    files received as input, with the files treated as a single text
    >>> d = build_semantic_descriptors_from_files(['animal_farm.txt'])
    >>> d['animal']['must']
    3
    >>> d['evil'] == {'all': 1, 'the': 1, 'habits': 1, 'of': 1, 'man': 1, 'are': 1}
    True
    >>> d = build_semantic_descriptors_from_files(['animal_farm.txt', 'alice.txt'])
    >>> 'king' in d['clever']
    True
    >>> 'brothers' in d['clever']
    True
    >>> len(d['man'])
    21
    
    >>> e = build_semantic_descriptors_from_files(['war_and_peace.txt'])
    >>> len(e['war'])
    2394
    '''
    #store the data
    data = []
    data_str = ''
    
    #read all files one by one and add them to the data_str
    for i in files:
        with open(i, "r", encoding="utf-8") as f:
            data_str += f.read()
            data_str += ' '
        f.close()
        
    #get word breakdown of the string
    list_of_words = get_word_breakdown(data_str)
    
    return get_all_semantic_descriptors(list_of_words)
