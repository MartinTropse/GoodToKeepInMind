# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:55:08 2019

@author: jernb
#Useful Links
#https://www.youtube.com/watch?v=8xoZuIwCmeI
#https://apps.sentinel-hub.com/eo-browser/
"""



from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date
from collections import OrderedDict
import pandas as pd
import os


try:
    api = SentinelAPI('johnjernberg', 'Lansstyrelsen', 'https://scihub.copernicus.eu/dhus')
    print("API connected")
except:
    print("API Error")

products = api.query(
               date=('20180712', '20180715'),
                  platformname='Sentinel-2', producttype='S2MSI2A',
                   cloudcoverpercentage=(0, 40))


products_df = api.to_dataframe(products)

dftile = products_df[products_df['filename'].str.contains("T33VWF")]

print(dftile.ingestiondate)
os.chdir(r'C:\Py\Sentinel')

try:
   api.download_all(dftile.index)
   print("Download complete")
except:
   print("Error downloading")
