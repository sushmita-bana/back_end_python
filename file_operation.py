one_file=open("one.txt",'r')
one_read=one_file.read()
for i in one_read:
    if i.isdigit()==True:
        a=(int(i))
print('a=',a)



two_file=open('two.txt','r')
two_read=two_file.read()
d=[]
for j in two_read:
    if j.isdigit()==True:
        b=int(j)
        d.append(b)
e=map(str,d)
f=list(e)
g=''.join(f)
h=int(g)
print('b=',h)

c=str(a+h)
print(c)



with open("three.txt","a+") as third:
    third.write('\n') 
    third.write("the sum of a and b is\t ")
    third.write(c)