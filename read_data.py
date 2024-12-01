import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

df = pd.read_csv('/Users/greysonmeyer/Desktop/Erdos_Work/omni_data_cleaned.csv')
print(df[['artwork_name', 'image_url']].head())