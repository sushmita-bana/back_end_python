def dict_lower(data):
    if len(data) == 1:
        return data.key.lower()
    else:
        for i in data:
            print(i.lower())
            if type(data[i]) is dict:
                for j in data[i]:
                    print(j.lower())
                    if type(data[i][j]) is dict:
                        for k in data[i][j]:
                            print(k.lower())


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
dict_lower(data)