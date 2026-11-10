mylist = [1,2,3,4,5,4,3,2,1]
mylist.append(5)
print(mylist)
mylist = [1,2,3,4,5,4,3,2,1]
mylist.extend([1,2,3,4,5,4,3,2,1])
print(mylist)
mylist = [1,2,3,4,5,4,3,2,1]
num=mylist[0]
print(num)
num2 = mylist[-1]
print(num2)
mylist = [1,2,3,4,5,4,3,2,1]
index = mylist.index(3)
print(index)
mylist = [1,2,3,4,5,4,3,2,1]
print(mylist)
index = 0
while index<len(mylist):
    element=mylist[index]
    print(f"The element of {index+1} term is {element}")
    index += 1
for i in mylist:
    print(i)

#or we can write

for i in range(len(mylist)):
    print(mylist[i])