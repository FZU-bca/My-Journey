set1={1,2,3}
set2={2,3,5}
set3=set1.difference(set2)
set4=set2.difference(set1)
print(set3)
print(set4)
set1.difference_update(set2)
print(set1)
set_1={1,2,3,4,5,6,7,8,9}
set_2={1,2,3,11,123,12313}
set_3=set_1.union(set_2)
print(set_3)
num=len(set_3)
print(num)
set_4={1,2,3,4,5,1,2,3,4,5}
num2=len(set_4)
print(num2)
#Set can not use WHILE sentence to see all, only FOR sentence
set1={1,2,3}
for item in set1:
    print(item)

my_list=['114514','114514','sakanaction','sakanaction','vaundy','vaundy']
my_set=set()
for item in my_list:
    my_set.add(item)
print(my_set)
