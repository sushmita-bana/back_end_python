def merge_half(list):
    if len(list)<=1:
        return list
    mid=len(list)//2
    left_list = list[:mid]
    right_list= list[mid:]
    left_list=merge_half(left_list)
    right_list=merge_half(right_list)
    return merge(left_list,right_list)
def merge(left_list,right_list):
    new_list=[]
    while len(left_list)!=0 and len(right_list)!=0:
        if left_list[0]<right_list[0]:
            new_list.append(left_list[0])
            left_list.remove(left_list[0])
        else:
            new_list.append(right_list[0])
            right_list.remove(right_list[0])
    if len(left_list)==0:
        new_list=new_list+right_list
    else:
        new_list=new_list+left_list
    return new_list


list=[4,3,7,5,6,9]
result=merge_half(list)
print(result)
