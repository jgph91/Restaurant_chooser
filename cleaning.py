import pandas as pd
from src.functions import rating_cleaner,tag_converter


database = pd.read_csv("./input/TA_restaurants_curated.csv")
df = pd.DataFrame(database)


df = df[['Name', 'City', 'Cuisine Style', 
         'Rating','URL_TA'
         ]]

df = df.rename(columns={"Cuisine Style":"tag"})
df['URL_TA'] = df['URL_TA'].apply(lambda x: 'https://www.tripadvisor.com' + x)


df['Rating']= df['Rating'].fillna('Unknown')
df['Rating'] = df['Rating'].apply(rating_cleaner)
df = df[(df['Rating'] != 'Unknown')]
df = df.sort_values('Rating',ascending = False)




df2= df['tag'].str.split(',',n = 7, expand = True)
df2 = df2.rename(columns={0:'tag1',1:'tag2',2:'tag3',3:'tag4',4:'tag5',5:'tag6'})


df2['tag1'] = tag_converter(df2['tag1'])
df2['tag2'] = tag_converter(df2['tag2'])
df2['tag3'] = tag_converter(df2['tag3'])
df2['tag4'] = tag_converter(df2['tag4'])
df2['tag5'] = tag_converter(df2['tag5'])
df2['tag6'] = tag_converter(df2['tag6'])

df = pd.concat([df,df2],axis=1)

df = df[['Name', 'City', 'Rating','URL_TA',
        'tag1','tag2','tag3','tag4','tag5']]


def query(city,tag):
    
    query = df[(
        (df['City'] == city) & ((df['tag1'] == tag) | (df['tag2'] == tag) | 
        (df['tag3'] == tag) | (df['tag4'] == tag) | (df['tag5'] == tag))
        )]

    return query.head(6)


