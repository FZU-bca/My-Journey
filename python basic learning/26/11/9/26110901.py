#.index
mylist=['dsadsadas','asdsadsadawfdsvf','python']
index = mylist.index('dsadsadas')
print(index)
#What if we search a index which is not in the list
# index = my_list1.index('yg8iifviyfd')
# print(index)


mylist[0] = "super"

print(f"The values is changed in {mylist[0]}")


#.insert
my_list=[1,2,3,4,5,6]
my_list.insert(1,"asd")
print(my_list)

#.append
my_list.append(7)
print(my_list)

#.extend

my_list.extend([8,9,10])
print(my_list)

#del
#.pop
del my_list[1]
print(my_list)


del1=my_list.pop(2)
print(del1)
print(my_list)


my_list=['it','py','su','ko','it','py']
my_list.remove('py')
print(my_list)


my_list.clear()
print(my_list)

my_list=['it','py','su','ko','it','py']
a=my_list.count('py')
print(a)
print(type(a))


b=len(my_list)
print(b)