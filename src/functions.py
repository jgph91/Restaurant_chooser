def rating_cleaner(text):
    '''Change the value of the incorrect ratings to Unknown'''

    dictionary = {-1.0: 'Unknown'}
    return dictionary.get(text,text)

def tag_converter (column):
    '''Normalize the tags column'''

    column = column.str.replace('[\[,\]]', '')
    column = column.str.strip('\'')
    column = column.str.strip()
    column = column.str.strip('\'')
    return column