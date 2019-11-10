import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

#gets the phone of each restaurant using web scraping.
def get_phone(url):
    
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html.parser')
    telephone = soup.find('body').text

    telephone = re.findall(r'\+[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+',telephone)[0]

    return phone
        

