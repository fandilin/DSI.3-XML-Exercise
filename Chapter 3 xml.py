
# coding: utf-8

# In[1]:

import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd


# In[2]:

document_tree = ET.parse( 'mondial_database.xml' )
root = document_tree.getroot()


# In[4]:

im = []
countries = []
for country in root.findall('country'):
    if country.findtext('infant_mortality') is None:
        continue
    else:
        im.append(float(country.findtext('infant_mortality')))
        countries.append(country.findtext('name'))


# In[5]:

im_df = pd.DataFrame({'Country':countries,'Infant Mortality':im})
im_df.sort_values('Infant Mortality').head(10)


# In[6]:

cities = []
citypops = []
for city in root.findall('country//city'):
    if city.findtext('population[last()]') is None:
        continue
    else:
        cities.append(city.findtext('name'))
        citypops.append(int(city.findtext('population[last()]')))


# In[7]:

citypops_df = pd.DataFrame({'City':cities,'Population':citypops})
citypops_df.sort_values('Population').tail(10)


# In[8]:

grouppops = []
groups = []
for country in root.findall('country'):
    for group in country.findall('ethnicgroup'):
        grouppops.append(float(group.get('percentage'))/100*float(country.findtext('population[last()]')))
        groups.append(group.text)


# In[9]:

groups_df = pd.DataFrame({'Ethnic Group':groups,'Population':grouppops})
groups_df.groupby('Ethnic Group').sum().sort_values('Population').tail(10)


# In[10]:

rivers = []
lengths = []
for river in root.findall('river'):
    if river.findtext('length') is None:
        continue
    else:
        lengths.append(float(river.findtext('length')))
        rivers.append(river.findtext('name'))


# In[11]:

rivers_df = pd.DataFrame({'River':rivers,'Length':lengths})
rivers_df.sort_values('Length').tail()


# In[12]:

lakes = []
areas = []
for lake in root.findall('lake'):
    if lake.findtext('area') is None:
        continue
    else:
        areas.append(float(lake.findtext('area')))
        lakes.append(lake.findtext('name'))


# In[13]:

lakes_df = pd.DataFrame({'Lake':lakes,'Area':areas})
lakes_df.sort_values('Area').tail()


# In[14]:

airports = []
elevations = []
for airport in root.findall('airport'):
    if airport.findtext('elevation') is '':
        continue
    else:
        elevations.append(float(airport.findtext('elevation')))
        airports.append(airport.findtext('name'))


# In[15]:

airports_df = pd.DataFrame({'Airport':airports,'Elevation':elevations})
airports_df.sort_values('Elevation').tail()


# In[ ]:



