def bubble(list):
    if len(list)==0:
        print('Empty list')
    else:
        for j in range(len(list)-1,0,-1):
            for i in range(j):
                if list[i]>list[i+1]:
                    temp=list[i]
                    list[i]=list[i+1]
                    list[i+1]=temp

list=[4,2,6,7,3,0]
bubble(list)
print(list)