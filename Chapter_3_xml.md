

```python
import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
```


```python
document_tree = ET.parse( 'mondial_database.xml' )
root = document_tree.getroot()
```


```python
im = []
countries = []
for country in root.findall('country'):
    if country.findtext('infant_mortality') is None:
        continue
    else:
        im.append(float(country.findtext('infant_mortality')))
        countries.append(country.findtext('name'))
```


```python
im_df = pd.DataFrame({'Country':countries,'Infant Mortality':im})
im_df.sort_values('Infant Mortality').head(10)
```
####These are the 10 countries with the lowest infant mortality rates.




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Infant Mortality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>36</th>
      <td>Monaco</td>
      <td>1.81</td>
    </tr>
    <tr>
      <th>90</th>
      <td>Japan</td>
      <td>2.13</td>
    </tr>
    <tr>
      <th>109</th>
      <td>Bermuda</td>
      <td>2.48</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Norway</td>
      <td>2.48</td>
    </tr>
    <tr>
      <th>98</th>
      <td>Singapore</td>
      <td>2.53</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Sweden</td>
      <td>2.60</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Czech Republic</td>
      <td>2.63</td>
    </tr>
    <tr>
      <th>72</th>
      <td>Hong Kong</td>
      <td>2.73</td>
    </tr>
    <tr>
      <th>73</th>
      <td>Macao</td>
      <td>3.13</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Iceland</td>
      <td>3.15</td>
    </tr>
  </tbody>
</table>
</div>




```python
cities = []
citypops = []
for city in root.findall('country//city'):
    if city.findtext('population[last()]') is None:
        continue
    else:
        cities.append(city.findtext('name'))
        citypops.append(int(city.findtext('population[last()]')))
```


```python
citypops_df = pd.DataFrame({'City':cities,'Population':citypops})
citypops_df.sort_values('Population').tail(10)
```
####These are the 10 cities with the largest populations.




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>977</th>
      <td>Shenzhen</td>
      <td>10358381</td>
    </tr>
    <tr>
      <th>1467</th>
      <td>Delhi</td>
      <td>11034555</td>
    </tr>
    <tr>
      <th>974</th>
      <td>Guangzhou</td>
      <td>11071424</td>
    </tr>
    <tr>
      <th>1252</th>
      <td>Tianjin</td>
      <td>11090314</td>
    </tr>
    <tr>
      <th>2594</th>
      <td>São Paulo</td>
      <td>11152344</td>
    </tr>
    <tr>
      <th>1250</th>
      <td>Beijing</td>
      <td>11716620</td>
    </tr>
    <tr>
      <th>443</th>
      <td>Moskva</td>
      <td>11979529</td>
    </tr>
    <tr>
      <th>1421</th>
      <td>Mumbai</td>
      <td>12442373</td>
    </tr>
    <tr>
      <th>707</th>
      <td>Istanbul</td>
      <td>13710512</td>
    </tr>
    <tr>
      <th>1251</th>
      <td>Shanghai</td>
      <td>22315474</td>
    </tr>
  </tbody>
</table>
</div>




```python
grouppops = []
groups = []
for country in root.findall('country'):
    for group in country.findall('ethnicgroup'):
        grouppops.append(float(group.get('percentage'))/100*float(country.findtext('population[last()]')))
        groups.append(group.text)
```


```python
groups_df = pd.DataFrame({'Ethnic Group':groups,'Population':grouppops})
groups_df.groupby('Ethnic Group').sum().sort_values('Population').tail(10)
```
####These are the 10 ethnic groups with the largest populations.




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Population</th>
    </tr>
    <tr>
      <th>Ethnic Group</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Malay</th>
      <td>1.219936e+08</td>
    </tr>
    <tr>
      <th>Japanese</th>
      <td>1.265342e+08</td>
    </tr>
    <tr>
      <th>Russian</th>
      <td>1.318570e+08</td>
    </tr>
    <tr>
      <th>Bengali</th>
      <td>1.467769e+08</td>
    </tr>
    <tr>
      <th>Mestizo</th>
      <td>1.577344e+08</td>
    </tr>
    <tr>
      <th>Dravidian</th>
      <td>3.027137e+08</td>
    </tr>
    <tr>
      <th>African</th>
      <td>3.183251e+08</td>
    </tr>
    <tr>
      <th>European</th>
      <td>4.948722e+08</td>
    </tr>
    <tr>
      <th>Indo-Aryan</th>
      <td>8.718156e+08</td>
    </tr>
    <tr>
      <th>Han Chinese</th>
      <td>1.245059e+09</td>
    </tr>
  </tbody>
</table>
</div>




```python
countrycodes = []
countrynames = []
for country in root.findall('country'):
    countrycodes.append(country.get('car_code'))
    countrynames.append(country.findtext('name'))
country_dict = dict(zip(countrycodes,countrynames))
```


```python
rivers = []
lengths = []
countries = []
for river in root.findall('river'):
    if river.findtext('length') is None:
        continue
    else:
        lengths.append(float(river.findtext('length')))
        rivers.append(river.findtext('name'))
        countries.append(', '.join(country_dict[x] for x in river.get('country').split(' ')))
```


```python
rivers_df = pd.DataFrame({'River':rivers,'Length':lengths,'Country':countries})
rivers_df.sort_values('Length').tail()
```
####These are the longest rivers.




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Length</th>
      <th>River</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>201</th>
      <td>Congo, Zaire</td>
      <td>4374.0</td>
      <td>Zaire</td>
    </tr>
    <tr>
      <th>123</th>
      <td>Russia</td>
      <td>4400.0</td>
      <td>Lena</td>
    </tr>
    <tr>
      <th>136</th>
      <td>China</td>
      <td>4845.0</td>
      <td>Hwangho</td>
    </tr>
    <tr>
      <th>137</th>
      <td>China</td>
      <td>6380.0</td>
      <td>Jangtse</td>
    </tr>
    <tr>
      <th>174</th>
      <td>Colombia, Brazil, Peru</td>
      <td>6448.0</td>
      <td>Amazonas</td>
    </tr>
  </tbody>
</table>
</div>




```python
lakes = []
areas = []
countries = []
for lake in root.findall('lake'):
    if lake.findtext('area') is None:
        continue
    else:
        areas.append(float(lake.findtext('area')))
        lakes.append(lake.findtext('name'))
        countries.append(', '.join(country_dict[x] for x in lake.get('country').split(' ')))
```


```python
pd.options.display.max_colwidth = 100
lakes_df = pd.DataFrame({'Lake':lakes,'Area':areas,'Country':countries})
lakes_df.sort_values('Area').tail()
```
####These are the largest lakes.




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area</th>
      <th>Country</th>
      <th>Lake</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>106</th>
      <td>57800.0</td>
      <td>United States</td>
      <td>Lake Michigan</td>
    </tr>
    <tr>
      <th>104</th>
      <td>59600.0</td>
      <td>Canada, United States</td>
      <td>Lake Huron</td>
    </tr>
    <tr>
      <th>79</th>
      <td>68870.0</td>
      <td>Tanzania, Kenya, Uganda</td>
      <td>Lake Victoria</td>
    </tr>
    <tr>
      <th>107</th>
      <td>82103.0</td>
      <td>Canada, United States</td>
      <td>Lake Superior</td>
    </tr>
    <tr>
      <th>54</th>
      <td>386400.0</td>
      <td>Russia, Azerbaijan, Kazakhstan, Iran, Turkmenistan</td>
      <td>Caspian Sea</td>
    </tr>
  </tbody>
</table>
</div>




```python
airports = []
elevations = []
countries = []
for airport in root.findall('airport'):
    if airport.findtext('elevation') is '':
        continue
    else:
        elevations.append(float(airport.findtext('elevation')))
        airports.append(airport.findtext('name'))
        countries.append(country_dict[airport.get('country')])
```


```python
airports_df = pd.DataFrame({'Airport':airports,'Elevation':elevations,'Country':countries})
airports_df.sort_values('Elevation').tail()
```
####These are the airports at the highest elevations.




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Airport</th>
      <th>Country</th>
      <th>Elevation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>789</th>
      <td>Teniente Alejandro Velasco Astete Intl</td>
      <td>Peru</td>
      <td>3311.0</td>
    </tr>
    <tr>
      <th>787</th>
      <td>Juliaca</td>
      <td>Peru</td>
      <td>3827.0</td>
    </tr>
    <tr>
      <th>230</th>
      <td>Yushu Batang</td>
      <td>China</td>
      <td>3963.0</td>
    </tr>
    <tr>
      <th>212</th>
      <td>Lhasa-Gonggar</td>
      <td>China</td>
      <td>4005.0</td>
    </tr>
    <tr>
      <th>80</th>
      <td>El Alto Intl</td>
      <td>Bolivia</td>
      <td>4063.0</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
