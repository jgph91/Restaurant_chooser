import pandas as pd
from src.functions import rating_cleaner,tag_converter

#Getting the databasfrom the csv file.

def clean_db(city,tag):
 
        database = pd.read_csv("./input/TA_restaurants_curated.csv")
        df = pd.DataFrame(database)

        # Selecting the columns used for answering the query and formating it.

        df = df[['Name', 'City', 'Cuisine Style', 
                'Rating','URL_TA','Number of Reviews'
                ]]

        df = df.rename(columns={"Cuisine Style":"tag"})
        df['URL_TA'] = df['URL_TA'].apply(lambda x: 'https://www.tripadvisor.com' + x)

        df['Rating']= df['Rating'].fillna('Unknown')
        df['Rating'] = df['Rating'].apply(rating_cleaner) #give the 'unknown' tag to incorrect values.
        df = df[(df['Rating'] != 'Unknown')] #taking out the 'unknown' rating from the main dataframe. 
        df = df.sort_values(['Rating','Number of Reviews'],ascending = [False,False])#sorting restaurants by rating and number of reviews

         #formating the tag column spliting it in new columns, in order to asign a tag for each column, for this task I had to create a new dataframe joining all the tags.
        df2= df['tag'].str.split(',',n = 7, expand = True)
        df2 = df2.rename(columns={0:'Tag1',1:'Tag2',2:'Tag3',3:'Tag4',4:'Tag5',5:'Tag6'})

        #giving format to the strings of the new columns
        df2['Tag1'] = tag_converter(df2['Tag1'])
        df2['Tag2'] = tag_converter(df2['Tag2'])
        df2['Tag3'] = tag_converter(df2['Tag3'])
        df2['Tag4'] = tag_converter(df2['Tag4'])
        df2['Tag5'] = tag_converter(df2['Tag5'])
        df2['Tag6'] = tag_converter(df2['Tag6'])

        #merging both dataframes into a single one
        df = pd.concat([df,df2],axis=1)
        #selecting the columns for the final dataframe, 'tag6' dropped because it contains a list of the remaining tags
        df = df[['Name', 'City', 'Rating','URL_TA',
                'Tag1','Tag2','Tag3','Tag4','Tag5']]

        #query function
        def query(city,tag):
                
                query = df[(
                (df['City'] == city) & ((df['Tag1'] == tag) | (df['Tag2'] == tag) | 
                (df['Tag3'] == tag) | (df['Tag4'] == tag) | (df['Tag5'] == tag))
                )]

                return query

        result = query(city,tag)
        result = result.head(5) # give back the 5 ones with highest rating and number of reviews
        
        return result

