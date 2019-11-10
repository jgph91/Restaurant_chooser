def rating_cleaner(text):
    dictionary = {-1.0: 'Unknown'}
    return dictionary.get(text,text)

def tag_converter (column):
    column = column.str.replace('[\[,\]]', '')
    column = column.str.strip('\'')
    column = column.str.strip()
    column = column.str.strip('\'')
    return column