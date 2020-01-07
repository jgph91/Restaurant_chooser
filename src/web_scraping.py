import requests
from bs4 import BeautifulSoup
import re

#gets the phone of each restaurant using web scraping.
def get_phone(url,city):
    
    #the phone number structure it's different in each country
    city_6 = ['Lyon','Paris']
    city_5 = ['Barcelona','Geneva','Copenhagen','Zurich','Madrid','Brussels','Stockholm','Oslo','Warsaw']
    city_4 = ['Lisbon','Rome','Luxembourg','Budapest','Dublin','Ljubljana','Bratislava','London','Athens','Edinburgh','Krakow','Oporto','Milan','Prague']
    city_3 = ['Helsinki','Berlin','Vienna','Hamburg','Munich','Amsterdam']

    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html.parser')
    telephone = soup.find('body').text

    if city in city_6:
        try:
            telephone = re.findall(r'\+[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+',telephone)[0]
            return telephone
        except:
            return 'Not found' 
    
    elif city in city_5:
        try:
            telephone = re.findall(r'\+[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+',telephone)[0]
            return telephone
        except:
            return 'Not found'

    elif city in city_4:
        try:
            telephone = re.findall(r'\+[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+',telephone)[0]
            return telephone
        except:
            return 'Not found'

    elif city in city_3:
        try:
            telephone = re.findall(r'\+[0-9]+\s[0-9]+\s[0-9]+',telephone)[0]
            return telephone
        except:
            return 'Not found'

def range_price(url):
    
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html.parser')
    body = soup.find('body').text

    try:

        range_price = re.findall(r'€[0-9]+\s\-\s€[0-9]+',body)[0]
        range_price = re.sub(r'€',"",range_price)
        range_price += " euros"
        return range_price

    except:

        return 'Not found.'

def phone_collector(result,city):
    '''Returns a list with the phone for each restaurant'''

    phone_list = []
    url_list = []
    #getting the phones of restaurant via web scraping
    url_1 = result.loc[0]['URL_TA']
    phone_1 = get_phone(url_1,city)
    phone_list.append(phone_1)
    url_list.append(url_1)

    url_2 = result.loc[1]['URL_TA']
    phone_2 = get_phone(url_2,city)
    phone_list.append(phone_2)
    url_list.append(url_2)

    url_3 = result.loc[2]['URL_TA']
    phone_3 = get_phone(url_3,city)
    phone_list.append(phone_3)
    url_list.append(url_3)

    url_4 = result.loc[3]['URL_TA']
    phone_4 = get_phone(url_4,city)
    phone_list.append(phone_4)
    url_list.append(url_4)

    url_5 = result.loc[4]['URL_TA']
    phone_5 = get_phone(url_5,city)
    phone_list.append(phone_5)
    url_list.append(url_5)

    return phone_list,url_list

def prices_collector(url_list):
    '''Returns a list with the range of prices for each restaurant'''

    # list for appending the phones and for adding it to the dataframe
    range_price_list = []
    #getting the phones of restaurant via web scraping
    range_price_1 = range_price(url_list[0])
    range_price_list.append(range_price_1)

    range_price_2 = range_price(url_list[1])
    range_price_list.append(range_price_2)

    range_price_3 = range_price(url_list[2])
    range_price_list.append(range_price_3)

    range_price_4 = range_price(url_list[3])
    range_price_list.append(range_price_4)

    range_price_5 = range_price(url_list[4])
    range_price_list.append(range_price_5)

    return range_price_list

