import requests
import urllib
import pandas as pd
import numpy as np

# read in datafile
data_path = './data/NOAA_StormEvents/'
df_events = pd.read_csv(data_path + 'StormEvents_2014_2024.csv')

# query for fips county code
fips = np.zeros(len(df_events['BEGIN_LAT']))
for i in range(len(fips)):
    lat = df_events['BEGIN_LAT'][i]
    lon = df_events['BEGIN_LON'][i]
    if np.isnan(lat) or np.isnan(lon):
        fips[i] = np.nan
    else:
        params = urllib.parse.urlencode({'latitude': lat, 'longitude':lon, 'format':'json'})
        url = 'https://geo.fcc.gov/api/census/block/find?' + params
        response = requests.get(url)
        data = response.json()
        fips[i] =  data['County']['FIPS']
df_events['FIPS'] = fips

# save to new csv file
df_events.to_csv(data_path + 'StormEvents_2014_2024_fips.csv')