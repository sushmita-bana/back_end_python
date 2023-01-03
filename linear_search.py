def linear_search(list1,n):
    for i in range (0,len(list1)):
        if list1[i]==n:
            print('found at position ',i)
            continue
        else:
            pass

list=[33,87,34,27,98]
list1=sorted(list)
print(list1)
n=98
linear_search(list1,n)