def insertion_sort(list):
    for i in range (0,len(list)-1):
        for j in range(i+1,0,-1):
            if list[j]<list[j-1]:
                temp=list[j]
                list[j]=list[j-1]
                list[j-1]=temp
        print(list)
list = [4, 2, 8, 5, 9, 7,11,3]
insertion_sort(list)
print(list)
