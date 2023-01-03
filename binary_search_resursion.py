def binary(list,l,u,n):
    if u<l:
        return None
    else:
        mid=(u+l)//2
        if list[mid]<n:
            return binary(list,mid+1,u,n)
        elif list[mid]>n:
            return binary(list,l,mid-1,n)
        else:
            return list[mid]
list=[10,20,30,40,50]
print(binary(list,0,5,10))
#print(binary(list,0,5,2))
