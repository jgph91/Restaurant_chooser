import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

#gets the phone of each restaurant using web scraping.
def get_phone(url,city):
    
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html.parser')
    telephone = soup.find('body').text

    if (city == 'Madrid') | (city == 'Barcelona'):
        try:
            telephone = re.findall(r'\+[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+',telephone)[0]
            return telephone
        except:
            return 'No phone number found :('
    elif (city == 'Athens'):
        try:
            telephone = re.findall(r'\+[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+',telephone)[0]
            return telephone
        except:
            return 'No phone number found :('


