import argparse
import pandas as pd 
import requests
from bs4 import BeautifulSoup
import re
from src.functions import rating_cleaner,tag_converter
from src.cleaning import clean_db
from src.web_scraping import get_phone


"""parser = argparse.ArgumentParser(description= 'Enter the city and a tag for looking for restaurants.')
parser.add_argument()"""

print()
print('Enter the city and a tag for looking for the best restaurants.')
#getting the dataframe with the 5 restaurant with the best restaurants that meet the tag given.

city = 'Athens'
tag = 'Mediterranean'

result = clean_db(city,tag)

#reseting the index of the results dataframe
result = result.reset_index() 

print('Search completed, looking for the phone numbers...')

# list for appending the phones and for merging with the dataframe
phone_list = []

url_1 = result.loc[0]['URL_TA']
phone_1 = get_phone(url_1,city)
phone_list.append(phone_1)

url_2 = result.loc[1]['URL_TA']
phone_2 = get_phone(url_2,city)
phone_list.append(phone_2)

url_3 = result.loc[2]['URL_TA']
phone_3 = get_phone(url_3,city)
phone_list.append(phone_3)

url_4 = result.loc[3]['URL_TA']
phone_4 = get_phone(url_4,city)
phone_list.append(phone_4)

url_5 = result.loc[0]['URL_TA']
phone_5 = get_phone(url_5,city)
phone_list.append(phone_5)

print('Phone numbers found!')
result['Phone_numbers'] = phone_list

print('These are the best restaurants in {} for {} food:'.format(city,tag))
print(result)
#print(len(phone_list))
















































"""if __name__ == '__main__':"""