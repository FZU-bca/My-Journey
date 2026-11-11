#The learning of set
#[] () "" {}
my_set={'Sakanaction','Vaundy','One or rock','Sakanaction','Vaundy','One or rock','Sakanaction','Vaundy','One or rock'}
my_set_empty=set()
print(my_set,type(my_set))
print(my_set_empty,type(my_set_empty))
#Set can be changed
my_set.add('Eureka')
my_set.add('Vaundy')#useless
print(my_set)
my_set.remove('One or rock')
print(my_set)
my_set={'Sakanaction','Vaundy','One or rock','Sakanaction','Vaundy','One or rock','Sakanaction','Vaundy','One or rock'}
element=my_set.pop()
print(element)
print(my_set)
my_set={'Sakanaction','Vaundy','One or rock','Sakanaction','Vaundy','One or rock','Sakanaction','Vaundy','One or rock'}
my_set.clear()
print(my_set)