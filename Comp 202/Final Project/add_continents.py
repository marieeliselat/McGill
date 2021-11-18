#Marie-Elise Latorre
#260981320
 
def get_iso_codes_by_continent(filename):
    '''
    (str) -> dict
    returns a dictionary mapping continents� names to a list of ISO codes of countries
    that belongs to that continent
    >>> d = get_iso_codes_by_continent("iso_codes_by_continent.tsv")
    >>> len(d['ASIA'])
    50
    >>> len(d['NORTH AMERICA'])
    23
    >>> d['AFRICA'][0]
    'NGA'
    >>> d['EUROPE'][2]
    'BLR'
    
    >>> d = get_iso_codes_by_continent("iso_codes_by_continent.tsv")
    >>> (d['SOUTH AMERICA'])
    ['URY', 'COL', 'BRA', 'GUY', 'ECU', 'VEN', 'PER', 'ARG', 'BOL', 'PRY', 'SUR', 'CHL']
    
    >>> d = get_iso_codes_by_continent("iso_codes_by_continent.tsv")
    >>> d['asia']
    KeyError: 'asia'
    '''
    continents = []
    i=0
    #open file and readlines
    #get rid of the last character of each line which is \n
    file = open(filename, "r", encoding="utf-8")
    continents += file.readlines()
    for line in continents:
        continents[i] = line[:-1]
        i += 1
    file.close()
    
    #split at tab
    temp_list = []
    for line in continents:
        temp_list.append(line.split('\t'))
        
    #make a dictionnary
    iso_code_dict = {}
    for entry in temp_list:
        if entry[1].upper() not in iso_code_dict: #if the key is not in iso_dict
            iso_code_dict[entry[1].upper()] = [] #create it in upper
            iso_code_dict[entry[1].upper()].append(entry[0]) #add it'svalue
        else:
            iso_code_dict[entry[1].upper()].append(entry[0]) #add the value
           
    return iso_code_dict
    
    
def add_continents_to_data(input_filename, continents_filename, output_filename):
    '''
    (str,str,str) -> int
    Change that should happen to the data is that in the output file a column should be added
    with the continent to which each country belongs
    Return an integer indicating the number of lines written to output_filename
    >>> add_continents_to_data("small_clean_co2_data.tsv", "iso_codes_by_continent.tsv",
    "small_co2_data.tsv")
    10
    >>> clean_one('input_practice.txt', 'outer_file_practice.tsv')
    23
    >>> clean_one('zero_text.tsv', 'zero_text_out.tsv')
    ''
    '''
    lines = []
    i = 0
    #read file by lines and get rid of \n
    file = open(input_filename, "r", encoding="utf-8")
    lines += file.readlines()
    for line in lines:
        lines[i] = line[:-1]
        i += 1
    file.close()
    
    #split at tab
    new_list = []
    for line in lines:
        new_list.append(line.split('\t'))
    
    #get dictionnary
    iso_code_dict = get_iso_codes_by_continent(continents_filename)
    
    #reverse the dictionnary so that all the keys become values and vice versa
    reversed_dictionary = {}
    for key in iso_code_dict.keys():
        for iso in iso_code_dict[key]:
            if iso in reversed_dictionary:
                reversed_dictionary[iso].append(key)
            else:
                reversed_dictionary[iso] = [key]
                
    #get the continent and add it to the new_list
    for line in new_list:
        for key in reversed_dictionary:
            if line[0] == key:
                line.insert(2, ','.join(reversed_dictionary[key]))
 
    #convert new_list into strings
    final_str = ''
    for sublist in new_list:
        final_str += '\t'.join(sublist)
        final_str += '\n'
 
    #write the string into the output filename
    fobj = open(output_filename, "w")
    fobj.write(final_str)
    fobj.close
 
    return(len(lines))
