#ggghweeeffssss
#3g1h1w3e2f4s
a=input('enter the string: ')
list2=[]
for char in a:
    list2.append(char)
print(list2)
list3=[]
for j in list2:
    if j not in list3:
        list3.append(j)
print(list3)
list4=[]
for i in list3:
    if a.count(i)>0:
        list4.append(a.count(i))
print(list4)
b=''.join(list3)
print(b)
list_string=map(str,list4)
d=list(list_string)
e=''.join(d)
print(e)
list5=[]
for i in range(len(b)):
    h=e[i]+b[i]
    list5.append(h)
print(list5)
g=''.join(list5)
print(g)