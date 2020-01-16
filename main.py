import argparse
import pandas as pd 
from src.cleaning import clean_db
from src.web_scraping import get_phone,range_price,phone_collector,prices_collector
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

    phone_list,url_list = phone_collector(result,args.city)
    #adding phone numbers to main dataframe
    result['Phone_numbers'] = phone_list

    print('Phone numbers found, getting the range of prices...')

    range_price_list = prices_collector(url_list)
    #adding range prices to main dataframe
    result['Range_Price'] = range_price_list
    #printing the result in terminal
    print('These are the best restaurants in {} for {} food:'.format(args.city,args.tag))
    result = result[['Name', 'City','Rating','Tag1','Tag2','Tag3','Tag4','Tag5','Phone_numbers','Range_Price']]
    print(result)

    print('Creating the pdf file...')
    pdf_creator(result)
    print('Ready! pdf saved in output folder.')

    #sending the pdf to your mail mail if you want to
    mail_sender()
    print('Email sent! Bon appétit! ')


if __name__ == '__main__':
    main()