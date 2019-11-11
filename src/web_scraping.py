import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

#gets the phone of each restaurant using web scraping.
def get_phone(url,city):
    
    #the phone number structure it's different in each country
    city_6 = ['Lyon','Paris']
    city_5 = ['Barcelona','Geneva','Copenhagen','Zurich','Madrid','Brussels','Stockholm','Oslo','Warsaw']
    city_4 = ['Lisbon','Rome','Luxembourg','Budapest','Dublin','Ljubljana','Bratislava','London','Athens','Edinburgh','Krakow','Oporto','Milan','Prague']
    city_3 = ['Helsinki','Berlin','Vienna','Hamburg','Munich']

    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html.parser')
    telephone = soup.find('body').text

    if city in city_6:
        try:
            telephone = re.findall(r'\+[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+',telephone)[0]
            return telephone
        except:
            return 'Phone number not found' 
    
    elif city in city_5:
        try:
            telephone = re.findall(r'\+[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+',telephone)[0]
            return telephone
        except:
            return 'Phone number not found'

    elif city in city_4:
        try:
            telephone = re.findall(r'\+[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+',telephone)[0]
            return telephone
        except:
            return 'Phone number not found'

    elif city in city_3:
        try:
            telephone = re.findall(r'\+[0-9]+\s[0-9]+\s[0-9]+',telephone)[0]
            return telephone
        except:
            return 'Phone number not found'

def range_price(url):
    
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html.parser')
    body = soup.find('body').text

    try:

        range_price = re.findall(r'€[0-9]+\s\-\s€[0-9]+',body)[0]
        return range_price

    except:

        return 'Range price not found.'

