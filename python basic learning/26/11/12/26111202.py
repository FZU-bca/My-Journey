from python.Lib.multiprocessing.dummy import dict

my_dic = {'ysw':99,'bca':98,'wqx':97}
my_dic2 = {}
my_dic3 = dict()
print(type(my_dic),type(my_dic2),type(my_dic3))
print(my_dic,my_dic2,my_dic3)
#There can not be the same keys in a dictionary
#And if there are twe same key, the value of key till be the lastest one
#Only by using key can search the value
#For example
stu_score = {'ysw':99,'bca':98,'wqx':97}
print(stu_score['ysw'],stu_score['bca'],stu_score['wqx'])
dict1={'project1':77,'project2':66,'project3':33}
dict2={'project1':88,'project2':86,'project3':55}
dict3={'project1':99,'project2':96,'project3':66}
mydict={'ysw':dict1,'bca':dict2,'wqx':dict3}
element1=mydict['ysw']['project1']
element2=mydict['bca']['project2']
element3=mydict['wqx']['project3']
print(mydict)
print(element1)
print(element2)
print(element3)