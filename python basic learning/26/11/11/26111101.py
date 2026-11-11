my_str="Sakanaction"
index=0
while index<len(my_str):
    print(my_str[index])
    index+=1

for i in my_str:
    print(i)


str1="itheima itcast boxuegu"
i=str1.count("it")
print(i)
newstr2=str1.replace(" ","|")
new_str=newstr2.split("|")
print(new_str)


#the using of sequence
mylist=[0,1,2,3,4,5,6,7,8,9]
my_list1=mylist[1:4]
print(my_list1)


mytuple=(0,1,2,3,4,5,6,7,8,9)
mytuple1=mytuple[:]
print(mytuple1)



mystr="0123456789"
mystr1=mystr[::2]
print(mystr1)
mystr2=mystr[::-1]
print(mystr2)


mylist2=mylist[6:3:-1]
print(mylist2)


mytuple2=mytuple[::-2]
print(mytuple2)
