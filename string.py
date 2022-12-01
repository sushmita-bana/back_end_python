#ggghweeeffssss
#3g1h1w3e2f4s

a=input('enter the string: ')
list0=[]
for i in a:
    if i not in list0:
        list0.append(i)
print(list0)

list1=[]
for i in list0:
    if a.count(i)>0:
        list1.append(a.count(i))
print(list1)


b=''.join(list0)
list_string=map(str,list1)
c=list(list_string)
d=''.join(c)

list2=[]
for i in range(len(list0)):
    e=d[i]+b[i]
    list2.append(e)

print(''.join(list2))
