name='sakanaction one or rock vaundy'
print(name[0])
print(name[-1])
#string is an unchangeable container
# name[1]=2
# print(name)
i=name.index('one or rock')
print(f"The beginning of 'one or rock' is {i}")
#replace
#replace all string1 into string2(the old string is not changed but create a new string:return value)
name_1=name.replace('one or rock','rock')
print(name_1)
print(name)
#split
#split string with determined thing, and return a list and in the meantime the old string will not be changed
my_str="hello python sakanaction vaundy"
element=my_str.split(' ')
print(element)
print(element[0])
print(my_str)
print(type(my_str))
print(type(element))
print(type(element[0]))
#strip
#string.strip
my_str='   What ever it takes    '
new_str=my_str.strip()
print(new_str)
print(my_str)
my_str='12What ever it takes21'
new_my_str=my_str.strip('12')
print(new_my_str)
print(my_str)
my_str='212What ever it takes221'
new_my_str=my_str.strip('212')
print(new_my_str)
my_str='What ever it takes'
i=my_str.count('at')
print(i)
length=len(my_str)
print(length)