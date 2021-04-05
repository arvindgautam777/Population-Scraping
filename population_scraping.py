import requests 
from bs4 import BeautifulSoup 
import csv
import re 

URL = "https://worldpopulationreview.com/#liveWorldPop"
page_dump = requests.get(URL) 

html_dump = BeautifulSoup(page_dump.content, 'html5lib') 
#print(soup.prettify())
World_Pop=[] # a list to store All Data 

def find_pop_Table(html_dump):
    Pop_table = html_dump.findAll('div', attrs = {'class' : 'datatableStyles__TableContainer-bwtkle-0 dvLKHZ'}) 
    print('I\'m here')
    for tag0 in Pop_table:
        Extract_text = tag0.find('a', attrs = { 'data-field': 'name'})
        print(Extract_text)
        if(Extract_text != None):
            if(re.match(r'Country', str(Extract_text.text))):
                return(tag0)
        
Pop_table = find_pop_Table(html_dump)



#print(Pop_table.prettify()) 

for tag in Pop_table.findAll('tr'): 
    #print(tag.prettify())
    Popul = {}
    try:
        Popul['flag'] = tag.img['src'] 
    except:
        Popul['flag'] = 'NA'
        pass
    try:
        Popul['Country'] = tag.a.text
    except:
        Popul['Country'] = 'NA'
        pass
    try:
        itag = tag.findAll('td')
        #print('The itag value is {}'.format(itag))
    except:
        pass
    try:
        Popul['Pop_2019'] = itag[3].text
        #print(itag[0].text)
    except:
        Popul['Pop_2019'] = 'NA'
        pass
    try:
        Popul['Area'] = itag[4].text
    except:
        Popul['Area'] = 'NA'
        pass
    try:
        Popul['Density_2019'] = itag[5].text
    except:
        Popul['Density_2019'] = 'NA'
        pass
    try:
        Popul['Growth_Rate'] = itag[6].text
    except:
        Popul['Growth_Rate'] = 'NA'
        pass
    try:
        Popul['World_Percentage'] = itag[7].text
    except:
        Popul['World_Percentage'] = 'NA'
        pass
    try:
        Popul['Rank'] = itag[8].text
    except:
        Popul['Rank'] = 'NA'
        pass
    try:
        World_Pop.append(Popul)
    except:
        pass

#print(World_Pop) 

file_Name = 'world_population.csv'


with open(file_Name, 'w')  as f: 
	handle = csv.DictWriter(f,['flag','Country','Pop_2019','Area','Density_2019', 'Growth_Rate','World_Percentage', 'Rank']) 
	handle.writeheader() 
	for country in World_Pop: 
		handle.writerow(country) 
        
f.close()
