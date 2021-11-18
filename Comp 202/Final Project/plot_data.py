#Marie-Elise Latorre
#260981320
 
import matplotlib.pyplot as plt
from build_countries import *
 
def get_bar_co2_pc_by_continent(dictionary, year):
    '''
    (dict, int) -> list
    create a bar plot representing the co2 emissions per capita (in tonnes) produced by all the countries
    in each continent
    Return a list of the values being plotted
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> get_bar_co2_pc_by_continent(d1, 2001)
    [0.20320332558992543, 67.01626016260163, 7.6609004739336495, 1.4196063588190764]
    
    >>> d1 = get_countries_from_file("america_countries.tsv")
    >>> get_bar_co2_pc_by_continent(d1, 2001)
    [0.20320332558992543, 67.01626016260163, 30.188626389018584]
    
    >>> d1 = get_countries_from_file("countries_in_South_America.tsv")
    >>> get_bar_co2_pc_by_continent(d1, 2002)
    [0.8881354122170013, 1.198976327575176, 1.9587971633593568]
    '''
    x_values = []
    y_values = []
    
    #keys = dictionary.keys()
 
    continents = Country.get_countries_by_continent(dictionary.values())
    
    # want to append the "lowest" value first
    # that means the "smallest" one in the alphabet first 
    for i in range(len(continents)):
        continent = min(continents)
        co2 = Country.get_total_co2_emissions_per_capita_by_year(continents[continent], year)
        y_values.append(co2)
        
        x_values.append(continent)
        continents.pop(continent)
        
 
    #print(x_values)
    #print(y_values)
        
    plt.bar(x_values, y_values)
    plt.ylabel('co2 (in tonnes)')
    plt.title('CO2 emissions per capita in' + str(year) + 'by marie-elise.latorre@mail.mcgill.ca')
    
    
    plt.savefig("co2_pc_by_continent_"+str(year)+".png")
 
    return (y_values)
    
 
def get_bar_historical_co2_by_continent(dictionary, year):
    '''
    (dict,int)-> list
    Create a bar plot representing the historical co2 emissions (in millions of tonnes) produced by
    all the countries in each continen
    Return a list of the values being plotted
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> get_bar_historical_co2_by_continent(d1, 2015)
    [4.877, 207.54500000000002, 359.367, 149.34300000000002]
    
    >>> d1 = get_countries_from_file("countries_i_like.tsv")
    >>> get_bar_historical_co2_by_continent(d1, 2015)
    [4.877, 4.877, 4.877, 4.877]
    
    >>> d1 = get_countries_from_file("countries_i_dislike.tsv")
    >>> get_bar_historical_co2_by_continent(d1, 2002)
    [9.746, 321.47803201, 26.3221, 103.91]
    
    '''
    x_values = []
    y_values = []
    
    #keys = dictionary.keys()
 
    continents = Country.get_countries_by_continent(dictionary.values())
    #print(continents)
    # want to append the "lowest" value first
    # that means the "smallest" one in the alphabet first 
    for i in range(len(continents)):
        continent = min(continents)
        co2 = Country.get_total_historical_co2_emissions(continents[continent], year)
        y_values.append(co2)
        x_values.append(continent)
        continents.pop(continent)
 
    #print(x_values)
    #print(y_values)
        
    plt.bar(x_values, y_values)
    plt.ylabel('co2 (in millions of tonnes)')
    plt.title('Historical CO2 emissions up to' + str(year) + 'by marie-elise.latorre@mail.mcgill.ca')
    
    
    plt.savefig("hist_co2_by_continent_"+str(year)+".png")
    return (y_values)
    
#d1 = get_countries_from_file("small_co2_data.tsv")
#print(get_bar_historical_co2_by_continent(d1, 2015))
def top_n_for_plot(dictionary, n, year):
    '''
    '''
    
    given_dict = copy.deepcopy(dictionary)
    emissions = []
    result = []
    temp_dict = {}
    
    for key, value in given_dict.items():
        co2 = value.co2_emissions
        
        population = value.population
        if co2.get(year) != None:
            calculation = (co2[year] * 1000000) / (population[year])
            temp_dict[calculation] = (key, value)
            print(key)
            print(value)
            emissions.append(calculation)
        else:
            continue
        
    emissions.sort()
    
    for emission in emissions:
        result.append((temp_dict[emission][0], emission))
         
    result = result[:n]
    return result
    
#d1 = get_countries_from_file("small_co2_data.tsv")
#print(top_n_for_plot(d1, 10, 2001))
 
def get_bar_co2_pc_top_ten(dictionary, year):
    '''
    (dict, int) -> list
    Return a list of the values being plotted
    Create a bar plot representing the co2 emissions per capita (in tonnes) produced by the top 10
    producing countries in the dictionary (if the dictionary contains less than 10 countries, then you
    should graph all of them)
    
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> data = get_bar_co2_pc_top_ten(d1, 2001)
    >>> len(data)
    5
    >>> data[0]
    67.01626016260163
    >>> data[4]
    0.20320332558992543
    '''
    
    lst_top_ten_tuples = top_n_for_plot(dictionary, 10, year)
    print(lst_top_ten_tuples)
    
    x_values = []
    y_values = []
    for i in lst_top_ten_tuples:
        x_values.append(i[0])
        y_values.append(i[1])
        
    x_values = x_values[::-1]
    y_values = y_values[::-1]
    
    plt.bar(x_values, y_values)
    plt.ylabel('co2 (in tonnes)')
    plt.title('Top 10 countries for CO2 emissions pc in' + str(year) + 'by marie-elise.latorre@mail.mcgill.ca')
    
    
    plt.savefig("hist_co2_by_continent_"+str(year)+".png")
    return (y_values)
