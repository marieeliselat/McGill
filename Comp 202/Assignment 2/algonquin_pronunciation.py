#Marie-Elise Latorre
#260981320
 
from algonquin_utils import *
 
PUNCTUATIONS = ["'",',',';',':','.','?','!','-'," "]
 
def get_consonant_pronunciation(x):
    """
    (str) -> str
    Return the consonants pronunciation
    Otherwise return an empty string
    >>> get_consonant_pronunciation('d')
    'D'
    >>> get_consonant_pronunciation('j')
    'GE'
    >>> get_consonant_pronunciation('r')
    ''
    """
    #check edge cases then check for membership in CONSONANTS and make it upper case
    if x == 'dj':
        return ('J')
    elif x == 'j':
        return ('GE')
    elif x in CONSONANTS:
        return (x.upper())
    else:
        return ""
    
def get_vowel_pronunciation(w):
    '''
    (str) -> str
    Return the vowel pronunciation
    Otherwise return an empty string
    >>> get_vowel_pronunciation("a")
    'A'
    >>> get_vowel_pronunciation("è")
    'E'
    >>> get_vowel_pronunciation("o")
    'U'
    '''
    
    w.lower() #lower case everything
    
    # convert VOWELS_WITH_ACCENT into a list
    list1=[]
    list1[:0] = VOWELS_WITH_ACCENT
    #make a list with what the VOWELS_WITH_ACCENT should sound like
    list2=['A','E','EE','O']
    #check edge cases then check for membership in VOWELS else make what VOWELS_WITH_ACCENT should sound like
    if w == 'o':
        return 'U'
    if w in VOWELS:
        return (w.upper())
    for i in range(len(list1)) :
        if list1[i] == w:
            list1[i] = list2[i] 
            return list2[i]
    else:
        return ' '
 
def get_diphthong_pronunciation(q):
    '''
    (str) -> str
    Return diphtong pronunciation
    Otherwise return an empty string
    >>> get_diphthong_pronunciation("ay")
    'EYE'
    >>> get_diphthong_pronunciation("ow")
    'OW'
    >>> get_diphthong_pronunciation("oy")
    ''
    '''
    
    q.lower() #lower case everything
    # convert DIPHTHONGS into a list
    list3=[]
    list3[:0] = DIPHTHONGS
    #make a list with what the DIPHTHONGS should sound like
    list4=['OW','EYE','AO','AY', 'EW', 'OW']
    #Make what the DIPHTHONGS should sound like
    for i in range(len(list3)) :
        if list3[i] == q:
            list3[i] = list4[i]
            return list4[i]
    else:
        return ''
   
 
def get_word_pronunciation(r):
    '''
    (str) -> str
    Return the word's pronunciation
    Otherwise return an empty string
    >>> get_word_pronunciation('kwey') # hello
    'KWAY'
    >>> get_word_pronunciation('madjashin') # see you later
    'MAJASHIN'
    >>> get_word_pronunciation('kasagiyan') # i love you
    'KASAGIYAN'
    '''
    
    pronunciation = ''
    r.lower()
    
    z = 0
    #check if r is a valid single word
    #check edge cases
    #then check for memberships and change sound accordingly 
    if is_valid_single_word(r):
        while z < len(r):
            if r[z] == 'd' and r[z+1]  == 'j':
                pronunciation += (get_consonant_pronunciation(r[z]+r[z+1]))
                z += 2
            elif r[z] in CONSONANTS:
                pronunciation += (get_consonant_pronunciation(r[z]))
                z += 1
            elif r[z] in VOWELS_WITH_ACCENT or r[z] in VOWELS:
                if r[z] == r[-1]:
                    pronunciation += (get_vowel_pronunciation(r[z]))
                    z += 1
                elif (r[z] == 'i' or r[z] == 'o') and r[z+1] == 'w': 
                    pronunciation += (get_diphthong_pronunciation(r[z]+r[z+1])) 
                    z += 2 
                elif (r[z] == 'i' or r[z] == 'o') and r[z+1] == 'y': 
                    pronunciation += (get_vowel_pronunciation(r[z])) 
                    z += 1 
                elif r[z+1] == 'y' or r[z+1] == 'w' : 
                    pronunciation += (get_diphthong_pronunciation(r[z]+r[z+1])) 
                    z += 2
                else:
                    pronunciation += (get_vowel_pronunciation(r[z]))
                    z += 1
            else:
                return ''
        return pronunciation
               
    else:
        return ""
 
 
 
def tokenize_sentence(h):
    '''
    (str) -> list
    Valid phrase break it down into strings representing either single words or a
    sequence of punctuation marks and space characters
    
    Returns a list containing all these strings
    
    >>> tokenize_sentence("a test")
    ['a', ' ', 'test']
    >>> tokenize_sentence("just__@a# test!")
    []
    >>> tokenize_sentence('Kwey') # Hello
    ['Kwey']
    >>> tokenize_sentence('Kwey, anin eji-pimadizin?') # Hello, how are you?
    ['Kwey', ', ', 'anin', ' ', 'eji', '-', 'pimadizin', '?']
    '''
    phrase=[]
    words=''
    punctuation = ''
    if is_valid_phrase(h):
        for r in range(len(h)):
            if h[r] in PUNCTUATIONS:
                if len(words) > 0:
                    phrase.append(words)
                    words =''
                punctuation += h[r]
            else:
                if len(punctuation)>0:
                    phrase.append(punctuation)
                    punctuation = ''
                words += h[r]
        if len(punctuation) >0:
            phrase.append(punctuation)
        elif len(words)>0:
            phrase.append(words)
        return phrase
    else:
        return []
            
def get_sentence_pronunciation(t):
    '''
    (str) -> str
    Return its pronunciation,
    Otherwise, return an empty string
    >>> get_sentence_pronunciation('Kwey') # Hello
    'KWAY'
    >>> get_sentence_pronunciation('Andi ejayan?') # Where are you going?
    'ANDI EGEEYEAN?'
    >>> get_sentence_pronunciation('Mino ishkwa nawakwe') # Good afternoon
    'MINU ISHKWA NOWAKWE'
    >>> get_sentence_pronunciation("I scream, you scream, we all scream for ice cream")
    ''
    '''
    Pronunciation = ''
    
    u = tokenize_sentence(t.lower())
    
    if is_valid_phrase(t):
        for char in u:
            if char in PUNCTUATIONS:
                Pronunciation += char
            else:
                Pronunciation += get_word_pronunciation(char)
    else:
        return ''
    
    return Pronunciation
        
