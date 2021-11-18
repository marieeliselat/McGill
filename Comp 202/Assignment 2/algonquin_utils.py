#Marie-Elise Latorre
#260981320

CONSONANTS = 'bcdghkmnpstwyzj'
VOWELS = 'aeio'
VOWELS_WITH_ACCENT = "àèìò"
PUNCTUATION = ',;:.?!-'
DIPHTHONGS = ['aw', 'ay', 'ew', 'ey', 'iw', 'ow']

def is_valid_consonant(a):
    """
    (str) -> bool
    Determines if it’s a single character representing a valid consonant in Algonquin
    >>> is_valid_consonant('j')
    True
    >>> is_valid_consonant('l')
    False
    >>> is_valid_consonant('G')
    True
    """
    a = a.lower() #lower case everything
    #check for membership
    return a in CONSONANTS

def is_valid_vowel(b):
    """
    (str) -> bool
    Determines if it’s a single character representing a valid vowel in Algonquin
    >>> is_valid_vowel('a')
    True
    >>> is_valid_vowel('ai')
    False
    >>> is_valid_vowel('h')
    False
    """
    b = b.lower()  #lower case everything
    #check for membership
    if (b in VOWELS) or (b in VOWELS_WITH_ACCENT):
        return True
    return False
    

def is_valid_single_word(c):
    """
    (str) -> bool
    Determines if it contains a single word made up by valid letters in Algonquin
    >>> is_valid_single_word('Kwey')
    True
    >>> is_valid_single_word('rats')
    False
    >>> is_valid_single_word('ay,dj')
    False
    """
    c = c.lower()  #lower case everything
    #check if c is a single word and not muliple words
    if "," in c or ' ' in c:
        return False
    
    #check every single character in str c is a valid consonnant or vowel
    for i in range(len(c)):
        for e in c:
            if is_valid_consonant(e) == True:
                #if it's the last character return
                if c[i] == c[-1]:
                    return True
            elif is_valid_vowel(e) == True:
                if c[i] == c[-1]:
                    return True
            else:
                return False
                
            
        
def is_valid_phrase(d):
    '''
    (str) -> bool
    Determines if it contains only valid letters in Algonquin, accepted punctuation marks, or space characters.
    >>> is_valid_phrase('Kwey') # Hello
    True
    >>> is_valid_phrase('Andi ejayan?') # Where are you going?
    True
    >>> is_valid_phrase('I scream, you scream, we all scream for ice cream')
    False
    '''
    #get rid of punctuations and spaces and covert phrase to one big word
    words = "" 
    for char in d:
        if char not in PUNCTUATION and char != " ":
            words += char
        
     #lower case everything and check if the whole thing is a valid single word
    if is_valid_single_word(words.lower()) == True:
        return True
    return False

#Marie-Elise Latorre
#260981320
 
CONSONANTS = 'bcdghkmnpstwyzj'
VOWELS = 'aeio'
VOWELS_WITH_ACCENT = "àèìò"
PUNCTUATION = ',;:.?!-'
DIPHTHONGS = ['aw', 'ay', 'ew', 'ey', 'iw', 'ow']
 
def is_valid_consonant(a):
    """
    (str) -> bool
    Determines if it’s a single character representing a valid consonant in Algonquin
    >>> is_valid_consonant('j')
    True
    >>> is_valid_consonant('l')
    False
    >>> is_valid_consonant('G')
    True
    """
    a = a.lower() #lower case everything
    #check for membership
    return a in CONSONANTS
 
def is_valid_vowel(b):
    """
    (str) -> bool
    Determines if it’s a single character representing a valid vowel in Algonquin
    >>> is_valid_vowel('a')
    True
    >>> is_valid_vowel('ai')
    False
    >>> is_valid_vowel('h')
    False
    """
    b = b.lower()  #lower case everything
    #check for membership
    if (b in VOWELS) or (b in VOWELS_WITH_ACCENT):
        return True
    return False
    
 
def is_valid_single_word(c):
    """
    (str) -> bool
    Determines if it contains a single word made up by valid letters in Algonquin
    >>> is_valid_single_word('Kwey')
    True
    >>> is_valid_single_word('rats')
    False
    >>> is_valid_single_word('ay,dj')
    False
    """
    c = c.lower()  #lower case everything
    #check if c is a single word and not muliple words
    if "," in c or ' ' in c:
        return False
    
    #check every single character in str c is a valid consonnant or vowel
    for i in range(len(c)):
        for e in c:
            if is_valid_consonant(e) == True:
                #if it's the last character return
                if c[i] == c[-1]:
                    return True
            elif is_valid_vowel(e) == True:
                if c[i] == c[-1]:
                    return True
            else:
                return False
                
            
        
def is_valid_phrase(d):
    '''
    (str) -> bool
    Determines if it contains only valid letters in Algonquin, accepted punctuation marks, or space characters.
    >>> is_valid_phrase('Kwey') # Hello
    True
    >>> is_valid_phrase('Andi ejayan?') # Where are you going?
    True
    >>> is_valid_phrase('I scream, you scream, we all scream for ice cream')
    False
    '''
    #get rid of punctuations and spaces and covert phrase to one big word
    words = "" 
    for char in d:
        if char not in PUNCTUATION and char != " ":
            words += char
        
     #lower case everything and check if the whole thing is a valid single word
    if is_valid_single_word(words.lower()) == True: 
        return True
    return False
