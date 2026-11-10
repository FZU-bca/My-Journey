#The learning of tuple
#tuple just like unchanged list
mytuple=(1,3,5,4,8,6,1,965,8546)
my_tuple=(1,"Hello",True)
t1=()
t2=tuple()
print(mytuple)
print(my_tuple)
print(t1)
print(t2)
print(type(t1))
print(type(t2))
t4=("Hello")
print(type(t4))
t5=("Hello", )
print(type(t5))
t5=("Hello",(1,2.4,456),('hdjkashdjk','asjdlasdja'))
print(t5)
print(type(t5))
i=t5[-1][0]
print(i)
t6=("FZU","TU",'FZU','MIEC','MIEC')
a=t6.count("FZU")
print(a)
b=len(t6)
print(b)
c=t6.index("FZU")
print(c)
t7=("FZU","TU",'FZU','MIEC','MIEC')
num=t7.count("FZU")
print(num)
t8=("FZU","TU",'FZU','MIEC','MIEC')
num2=len(t8)
print(num2)


index = 0
while index < len(t8):
    print(t8[index])
    index+=1
print()
for index in t8:
    print(index)



#Try to change tuple
# t8[0]="FZU"
# print(t8)


t1=(1,2,["dasdasdas","dasfsgageqq"])
print(t1)
t1[2][1]="nglksdgwer"
print(t1)


#intotal the biggest difference between list and tuple is that the tuple can not be changed
#BUt if there are a list in one tuple, the elements in list can be changed

