mylist=[1,2,3,4,5,6,7,8,9,10]
i=[]
for num in mylist:
    if num%2==0:
        i.append(num)
print(i)

i=[]
r=0
while r<10:
    if(mylist[r]%2==0):
        i.append(r+1)
    r+=1
print(i)



