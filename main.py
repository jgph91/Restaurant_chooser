import argparse
import pandas as pd 
from src.cleaning import clean_db
from src.web_scraping import get_phone,range_price
from src.pdf import pdf_creator
from src.mail import mail_sender

def parse():
    parser = argparse.ArgumentParser() 
    parser.add_argument('city', help='Enter the city where do you want to eat, check the available cities in the README file.', type= str)
    parser.add_argument('tag', help='Enter the type of food/restaurant that you are interested in, check the available tags in the README file.', type= str)
    return parser.parse_args()

def main():
    args  = parse()
    #getting the dataframe with the 5 restaurant with the best restaurants that meet the tag given.
    result = clean_db(args.city,args.tag)
    print('Search completed, looking for the phone numbers...')
    # list for appending the phones and for adding it to the dataframe
    phone_list = []
    #getting the phones of restaurant via web scraping
    url_1 = result.loc[0]['URL_TA']
    phone_1 = get_phone(url_1,args.city)
    phone_list.append(phone_1)

    url_2 = result.loc[1]['URL_TA']
    phone_2 = get_phone(url_2,args.city)
    phone_list.append(phone_2)

    url_3 = result.loc[2]['URL_TA']
    phone_3 = get_phone(url_3,args.city)
    phone_list.append(phone_3)

    url_4 = result.loc[3]['URL_TA']
    phone_4 = get_phone(url_4,args.city)
    phone_list.append(phone_4)

    url_5 = result.loc[4]['URL_TA']
    phone_5 = get_phone(url_5,args.city)
    phone_list.append(phone_5)

    #adding phone numbers to main dataframe
    result['Phone_numbers'] = phone_list
    print('Phone numbers found, getting range prices...')

    # list for appending the phones and for adding it to the dataframe
    range_price_list = []
    #getting the phones of restaurant via web scraping
    range_price_1 = range_price(url_1)
    range_price_list.append(range_price_1)

    range_price_2 = range_price(url_2)
    range_price_list.append(range_price_2)

    range_price_3 = range_price(url_3)
    range_price_list.append(range_price_3)

    range_price_4 = range_price(url_4)
    range_price_list.append(range_price_4)

    range_price_5 = range_price(url_5)
    range_price_list.append(range_price_5)
    #adding range prices to main dataframe
    result['Range_Price'] = range_price_list
    #printing the result in terminal
    print('These are the best restaurants in {} for {} food:'.format(args.city,args.tag))
    result = result[['Name', 'City','Rating','Tag1','Tag2','Tag3','Tag4','Tag5','Phone_numbers','Range_Price']]
    print(result)

    print('Creating pdf version...')
    pdf_creator(result)
    print('Ready! pdf saved in output folder.')
    #sendin the pdf mail if you want to
    mailing = input('Doy you want to receive the pdf via mail?(Y/N)')
    if mailing == "Y":
        mail_sender()
    else:
        print('Bon appétit!')

if __name__ == '__main__':
    main()