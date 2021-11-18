#Marie-Elise Latorre
#260981320
from vectors_utils import *
from similarity_measures import *
from file_processing import *
import matplotlib.pyplot as plt
 
 
def most_sim_word(word, choices, semantic_descriptors, similarity_fn):
    '''
    (str, list, dict, function) -> str
    returns the element of choices which has the largest semantic similarity to word,
    with the semantic similarity computed using the data in
    semantic_descriptors and the similarity function similarity_fn
    >>> choices = ['dog', 'cat', 'horse']
    >>> c = {'furry' : 3, 'grumpy' : 5, 'nimble' : 4}
    >>> f = {'furry' : 2, 'nimble' : 5}
    >>> d = {'furry' : 3, 'bark' : 5, 'loyal' : 8}
    >>> h = {'race' : 4, 'queen' : 2}
    >>> sem_descs = {'cat' : c, 'feline' : f, 'dog' : d, 'horse' : h}
    >>> most_sim_word('feline', choices, sem_descs, get_cos_sim)
    'cat'
    >>> most_sim_word('dog', choices, sem_descs, get_euc_sim )
    'dog'
    
    >>> choices = ['soup', 'cheese', 'water']
    >>> c = {'eat' : 3, 'liquid' : 5, 'chicken' : 4}
    >>> f = {'eat' : 3, 'tomato' : 4}
    >>> d = {'eat' : 1, 'brie' : 15, 'yellow' : 1}
    >>> h = {'transparent' : 4, 'drink' : 2}
    >>> sem_descs = {'broth' : c, 'soup' : f, 'cheese' : d, 'water' : h}
    >>> most_sim_word('broth', choices, sem_descs, get_norm_euc_sim )
    'soup'
    
    >>> choices = ['soup', 'cheese', 'water']
    >>> c = {'eat' : 10, 'liquid' : 1, 'chicken' : 1}
    >>> f = {'eat' : 3, 'tomato' : 4}
    >>> d = {'eat' : 3, 'brie' : 10, 'yellow' : 4}
    >>> h = {'transparent' : 2, 'drink' : 6}
    >>> sem_descs = {'broth' : c, 'soup' : f, 'cheese' : d, 'water' : h}
    >>> most_sim_word('broth', choices, sem_descs, get_norm_euc_sim )
    'soup'
    '''
    similarity = []
    if word not in semantic_descriptors.keys(): #return blank string id the word is not in the semantic_descriptors keys
        return ''
    for i in choices: #iterate through the list
        if i not in semantic_descriptors.keys(): 
            similarity.append(float('-inf')) #append - inf if the word of the list is not in semantic_descriptors keys
        else:
            try: 
                similarity.append(similarity_fn(semantic_descriptors[i], semantic_descriptors[word]))
            except: #catch -> if not working append - inf
                similarity.append(float('-inf')) 
    
    maximum = max(similarity) # get the maximum
    sim_index = similarity.index(maximum)
    
    return choices[sim_index]
 
def run_sim_test(filename, semantic_descriptors, similarity_fn):
    '''
    (str,, dict, function) -> float
    Returns the percentage (i.e., float between 0.0 and 100.0) of questions on which
    most_sim_word guesses the answer correctly using the semantic descriptors stored in semantic_descriptors,
    and the similarity function similarity_fn
    >>> descriptors = build_semantic_descriptors_from_files(['test.txt'])
    >>> run_sim_test('test.txt', descriptors, get_cos_sim)
    15.0
    
    >>> descriptors = build_semantic_descriptors_from_files(['test.txt'])
    >>> run_sim_test('test.txt', descriptors, get_norm_euc_sim)
    5.0
    
    >>> >>> descriptors = build_semantic_descriptors_from_files(['test.txt'])
    >>> run_sim_test('test.txt', descriptors, get_euc_sim)
    7.5
    '''
    fobj = open(filename, "r")
    in_reality = 0
    total = 0
    
    for i in fobj:
        temporary_string = ''
        temporary_string += i.strip() #strip the file and add it to the empty string
        temporary_string = temporary_string.split(' ') #split it at the blanks 
        most_similar = most_sim_word(temporary_string[0] , temporary_string[2:], semantic_descriptors, similarity_fn)
        if temporary_string[1] == most_similar:
            total += 1
        in_reality += 1
    fobj.close()
    
    return (total/in_reality) * 100
 
    
def generate_bar_graph(graph_list, filename):
    '''
    (list, str) -> void
    Generates a bar graph (using matplotlib) where the performance
    of each function on the given file test is plotted.
    
    Saves a picture of the bar graph under the name "synonyms_test_results".
    The graph has three bars comparing the differences of each similarity 
    '''
    descriptors = build_semantic_descriptors_from_files(['swanns_way.txt', 'war_and_peace.txt'])
    result = []
    for i in graph_list: 
        z = run_sim_test(filename, descriptors, i)
        result.append(z) 
    for i in range(len(graph_list)): 
        graph_list[i] = graph_list[i].__name__
        
    
    plt.bar(graph_list,result) #bar graph
    plt.title("Performance of each function on the given file test") #title
    plt.savefig("synonyms_test_results.png") #save it
