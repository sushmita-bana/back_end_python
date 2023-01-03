def dict_lower_main_key(data):

    for i in data:
        print(i.lower())
        if type(data[i]) is dict:
            print( dict_lower_nested_key(data[i]))
        else:
            continue
        #return dict_lower_main_key(i)

def dict_lower_nested_key(data):

    for k,v in data.items():
        print(k.lower())
        if type(v) is dict:
            return dict_lower_nested_key(v)

        else:
            return ''

data={
    'ZSAZ': 54678,
    'ZASAF':{
        'DAFFSS':87658,
        'GSSHHS':4774744,
        'GHDHGAA':{
            'HHHGAHA':678543,
            'GHAHHHHA':92678
        },
        'JHHJAH':738765
    },
    'HJKSHA':{
        'HGHAAGHA':985678
    },
    'GHGHAHA':674398
}
print(dict_lower_main_key(data))
#print(dict_lower_nested_key(data))





