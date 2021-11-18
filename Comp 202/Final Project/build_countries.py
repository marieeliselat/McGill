#Marie-Elise Latorre
#260981320
 
import copy
class Country:
    min_year_recorded = 99999
    max_year_recorded = -1
    '''
    Represents a country
    
    Instance Attributes: iso_code(str), name(str), continents(list),
                         co2_emissions(dict), population(dict)  
    
    '''
    def __init__(self, iso_code, name, continents, year, emissions, population):
        if (iso_code != 'OWID_KOS' and len(iso_code)!= 3):
            raise AssertionError
        self.co2_emissions = {year: emissions}
        self.population = {year: population}
        self.name = name
        self.iso_code= iso_code
        self.continents = copy.deepcopy(continents)
        if emissions !=  -1 or emissions !=  ' ':
            self.co2_emissions[year] = emissions
        if population != -1 or population != ' ':
            self.population[year] = population
        if year>Country.max_year_recorded:
            Country.max_year_recorded = year
        if year<Country.min_year_recorded:
            Country.min_year_recorded = year
 
    def __str__(self):
        '''
        (Country) -> str
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> str(r)
        'Russia\\tASIA,EUROPE\\t{2007: 1604.778}\\t{2007: 14266000}'
        
        >>> r = Country('QAT', 'Qatar', ['ASIA'], 2001, 41.215,  615000)
        >>> str(r)
        'Qatar\\t['ASIA']\\t{2001: 41.215}\\t{2001: 615000}'
        
        >>> t = Country('COD', 'Democratic Republic of Congo', ['AFRICA'],  2006,  1.553, 56578000)
        >>> str(t)
        'Democratic Republic of Congo\\t['AFRICA']\\t{2006: 1.553}\\t{2006: 56578000}'
        '''
        year = list(self.co2_emissions.keys())[0]
        if len(self.continents) == 2:
             continents_str = ','.join(self.continents)
        else:
            continents_str = self.continents[0]
        return (self.name + '\t' + continents_str + '\t' + str(self.co2_emissions) + '\t' + str(self.population))
        
    def add_yearly_data(self, data):
        '''
        (Country) -> NoneType
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> a.co2_emissions == {1949: 0.015, 2018: 9.439}
        True
        
        >>> a = Country("QAT", "Qatar", ["ASIA"], 2001, 41.215, 615000)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> print(a.co2_emissions)
        {2001: 41.215, 2018: 9.439}
        
        >>> a = Country("QAT", "Qatar", ["ASIA"], 2001, 41.215, 615000)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> print(a.population)
        {2001: 615000, 2018: 37122000}
        '''
        new_data = data.split('\t')
        year = int(new_data[0])
       
        if new_data[1] != '' or new_data[1] != -1:
            co2_emissions = float(new_data[1])
            self.co2_emissions[year] = co2_emissions
        if new_data[2] != '' or new_data[2] != -1:
            population = int(new_data[2])
            self.population[year] = population
        if year>Country.max_year_recorded:
            Country.max_year_recorded = year
        if year<Country.min_year_recorded:
            Country.min_year_recorded = year
 
    def get_co2_emissions_by_year(self,year):
        '''
        (Country, int) -> float
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> a.get_co2_emissions_by_year(1949)
        0.015
        
        >>> a = Country("QAT", "Qatar", ["ASIA"], 2001, 41.215, 615000)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> a.get_co2_emissions_by_year(2001)
        41.215
        
        >>> a = Country("QAT", "Qatar", ["ASIA"], 2001, 41.215, 615000)
        >>> a.add_yearly_data("2018\t9.439\t37122000")
        >>> print(a.get_co2_emissions_by_year(1949))
        0.0
        '''
        if year in self.co2_emissions.keys():
            return self.co2_emissions[year]
        else:
            return 0.0
        
    def get_co2_per_capita_by_year(self,year):
        '''
        '''
        if year not in self.co2_emissions or year not in self.population:
            return None
        else:
            temp = (self.co2_emissions[year]*1000000)
            result = temp/self.population[year]
            return result
    
        
    def get_historical_co2(self,year):
        '''
        '''
        years = list(self.co2_emissions.keys())
        temp = 0.0
        for i in years:
            if i <= year:
                temp+=self.co2_emissions[i]
        return temp
            
    @classmethod
    def get_country_from_data(cls,data):
        '''
        '''
        new_data = data.split('\t')
        continent = new_data[2].split(',')
        if new_data[4] == '':
            co2_emissions = -1
        else:
            co2_emissions = float(new_data[4])
            
        if new_data[5] == '':
            population = -1
        else:
            population = int(new_data[5])
        
        return cls(new_data[0],new_data[1],continent,int(new_data[3]),co2_emissions,population)
 
    @staticmethod
    def get_countries_by_continent(data):
        temp = {}
        for i in data:
            for j in i.continents:
                #print(continents)
                if j in temp:
                    #list(temp.keys())
                    temp[j].append(i)
                else:
                    temp[j] = [i]
        return temp
                
    @staticmethod
    def get_total_historical_co2_emissions(data,year):
        total = 0
        for i in data:
            total+=i.get_historical_co2(year)
        return total
        
    @staticmethod
    def get_total_co2_emissions_per_capita_by_year(data,year):
        '''
        If one of the two data point (co2 or population) is missing for a country in the list, then this
        country should be excluded when computing the value needed. More over, if the total co2 or the
        total population is 0, then the function should return 0.0.
        '''
        co2 = 0
        population = 0
        
        for i in data:
 
            if i.get_co2_per_capita_by_year(year)!= None:
                co2 += i.get_co2_emissions_by_year(year)
                population += i.population[year]
        temp = ((co2)*1000000)/ population
        return temp
            
    @staticmethod
    def get_co2_emissions_per_capita_by_year(data,year):
        temp = {}
        
        for i in data:
            temp[i] = i.get_co2_per_capita_by_year(year)
            
        return temp
        
    @staticmethod
    def get_historical_co2_emissions(data, year):
        temp = {}
        for i in data:
            temp[i] = i.get_historical_co2(year)
        return temp
    
    @staticmethod
    def get_top_n(dictionary, n):
        given_dict = copy.deepcopy(dictionary)
        names_of_countries = []
        result = []
        
        for key, value in given_dict.items():
            names_of_countries.append((-value, key.name, key.iso_code))
            
        names_of_countries.sort()
        
        for i in names_of_countries:
            result.append((i[2], -i[0]))
            
        result = result[:n]
        return result
 
        
def get_countries_from_file(filename):
    '''
    (str) -> dict
    Creates and return a dictionary mapping ISO country codes (strings)
    to objects of type Country based on the data in the file
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> len(d1)
    9
    >>> str(d1['ALB'])
    'Albania\\tEUROPE\\t{2002: 3.748}\\t{2002: 3126000}'
    '''
    lines = []
    i = 0
    #read file by lines and get rid of \n
    file = open(filename, "r", encoding="utf-8")
    lines += file.readlines()
    for line in lines:
        lines[i] = line[:-1]
        i += 1
    if lines[-1] == '':
        lines.remove(lines[-1])
    file.close()
 
    
    final_dict = {}
    for line in lines:
        line = line.strip('\n')
        data = line.split('\t')
        iso = data[0]
        if iso not in final_dict:
            final_dict[iso] = Country.get_country_from_data(line)
        else:
            else_data = '\t'.join(data[3:])
            
            final_dict[iso].add_yearly_data(else_data)
        
    return(final_dict)
