def selection_sort(list):
   for i in range(0,len(list)):
      min_index = i
      for j in range(i+1,len(list)):
         if list[min_index]>list[j]:
            min_index=j
            list[i]=list[min_index]
            list[min_index]=list[i]

list=[4,3,6,5,8,1]
selection_sort(list)
print(list)