#Marie-Elise Latorre
#260981320
 
def find_delim(string):
    '''
    (str) -> str
    Returns the most commonly used delimiter in the input string
    >>> find_delim("0 1 2 3,4")
    ' '
    >>> find_delim('AmericanBoy')
    Assertion Error: None of the delimeters are used
    >>>find_delim('My\tfavorite\tsubject\tis math,I like,doing,problems.')
    ','
    '''
    num_comas = string.count(',')
    num_spaces = string.count(' ')
    num_tab = string.count('\t')
    num_dashes = string.count('-')
    
    try:
        assert num_comas != 0 or num_spaces!= 0 or num_tab != 0 or num_dashes != 0, "Assertion Error: None of the delimeters are used"
        if num_comas>= num_spaces and num_comas >= num_tab and num_comas >= num_dashes:
            return ','
        elif num_spaces>= num_comas and num_spaces >= num_tab and num_spaces >= num_dashes:
            return ' '
        elif num_tab>= num_comas and num_tab >= num_spaces and num_tab >= num_dashes:
            return '\t'
        else:
            return '-'
    except AssertionError as st:
        print(st)
 
 
def clean_one(input_filename, output_filename):
    '''
    (str, str) -> int
    - The output_filename will have instead of the most common delimeter, a tab
    - Return an integer indicating the number of lines written to output_filename
    >>> clean_one('small_raw_co2_data.txt', 'small_tab_sep_co2_data.tsv')
    10
    >>> clean_one('input_practice.txt', 'outer_file_practice.tsv')
    23
    >>> clean_one('zero_text.tsv', 'zero_text_out.tsv')
    ''
    '''
    lines = []
        
    #open file and read all the lines
    #add those lines to an empty list
    f = open(input_filename, "r", encoding="utf-8")
    lines += f.readlines() 
    f.close()
    
    #add to an empty string the modified content
    #modified content = replacing the most common delimeter with tab at each line
    new_data = ''
    
    for i in lines:
        new_data += i.replace(find_delim(i), '\t')
 
 
        
    #write the new_data into the output file
    fobj = open(output_filename, "w")
    fobj.write(new_data)
    fobj.close
    
    #check how many lines there are
    return len(lines)
 
    
def final_clean(input_filename, output_filename):
    '''
    (str,str) -> int
    - All decimal numbers will have a dot instead of a comma
    - There should only be 5 columns, so if there are more get rid of them
    - Return an integer indicating the number of lines written to output_filename
    >>> final_clean('small_tab_sep_co2_data.tsv', 'small_clean_co2_data.tsv')
    10
    >>> clean_one('input_practice.txt', 'outer_file_practice.tsv')
    23
    >>> clean_one('zero_text.tsv', 'zero_text_out.tsv')
    ''
    '''
    
    clean_one(input_filename, output_filename)
    
    #open file and read the lines
    #append those lines to an empty list
    lines = []
    f = open(output_filename, "r", encoding="utf-8")
    lines += f.readlines() 
    f.close()
    
    #split the list at tab
    new_list = []
    for line in lines:
        new_list.append(line.split('\t'))
 
    #combine the words when needed
    for line in new_list:
        while line[2].isdigit() == False:
            line[1] += ' ' 
            line[1] += line.pop(2)
        
    
    #replace the decimal comma by a dot        
    for line in new_list:
        if len(line)> 5:
            line[3] += '.'
            line[3] += line.pop(4)
        elif ',' in line[3]:
            for character in line[3]:
                line[3] = line[3].replace(',','.')
    
    
    #add to an empty string
    final_str = ''
    for sublist in new_list:
        final_str += '\t'.join(sublist)
    
    
    #write the string into the output file
    fobj = open(output_filename, "w")
    fobj.write(final_str)
    fobj.close
    
    #return how many lines there are
    return len(lines)
