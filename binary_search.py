pos=-1
def binary(sorted_n,data):
    l=0
    u=len(sorted_n)-1

    while l<=u:
        mid = (u + l) // 2
        if sorted_n[mid]==data:
            globals()['pos']=mid
            return True
        else:
            if sorted_n[mid]<data:
                l=mid+1
            else:
                u=mid-1
    return False

n=[5,3,6,10,2,9,7]
sorted_n=sorted(n)
print(sorted_n)
data=10
if binary(sorted_n,data):
    print('available',pos)
else:
    print('not available')
