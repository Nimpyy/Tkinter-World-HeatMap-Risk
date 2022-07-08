import pandas as pd
import geopandas as gpd
import sys
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.colors as colors
import country_converter as coco
matplotlib.use("TkAgg")


sources = pd.read_csv(r"path to data sample", encoding = 'ISO-8859-1')
colsource = list(sources.columns.values)

df = pd.read_csv('Total_Score_Countries_Sample', encoding = 'ISO-8859-1')
cols = list(df.columns.values)

SHAPEFILE = r'path to the shapefile'

geo_df = gpd.read_file(SHAPEFILE)[['ADMIN', 'ADM0_A3', 'geometry']]
geo_df_columns = ['country', 'CODE', 'GEONMETRY']
geo_df = geo_df.drop(geo_df.loc[geo_df['ADMIN'] == 'Antarctica'].index)

iso3_codes = geo_df['ADMIN'].to_list()
iso2_codes_list = coco.convert(names=iso3_codes, to='ISO2', not_found='NULL')

geo_df['iso2_code'] = iso2_codes_list
geo_df = geo_df.drop(geo_df.loc[geo_df['iso2_code'] == 'NULL'].index)

df = df.sort_values('ADMIN') 

#merge the shapefile and the score data 
merged_df = pd.merge(left=geo_df.sort_values('ADMIN'), right=df.sort_values('ADMIN'), on="ADMIN")
