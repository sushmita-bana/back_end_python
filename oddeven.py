list=[3,2,5,6,4,8,7,9]

for i in range(len(list)):
    if list[i]%2!=0:
        list.append(list[i])
        list.remove(list[i])
print(list)