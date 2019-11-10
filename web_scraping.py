import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def get_phone():
    url = 'https://www.tripadvisor.com/Restaurant_Review-g187514-d15364769-Reviews-La_Gaditana_Castellana-Madrid.html'
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html.parser')
    telephone = soup.find('body').text

    telephone = re.findall(r'\+[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+',telephone)[0]

    return phone
        

