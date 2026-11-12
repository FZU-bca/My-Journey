dict1={'project1':77,'project2':66,'project3':33}
dict2={'project1':88,'project2':86,'project3':55}
dict3={'project1':99,'project2':96,'project3':66}
mydict={'ysw':dict1,'bca':dict2,'wqx':dict3}
mydict['cby']={'project1':97,'project2':86,'project3':43}
print(mydict['cby']['project1'])
mydict['ysw']['project1']=20
print(mydict['ysw']['project1'])
score1=mydict['ysw'].pop('project1')
print(score1)
print(mydict)

mydict.clear()
print(mydict)

dict1={'project1':77,'project2':66,'project3':33}
dict2={'project1':88,'project2':86,'project3':55}
dict3={'project1':99,'project2':96,'project3':66}
mydict={'ysw':dict1,'bca':dict2,'wqx':dict3}
keys=mydict.keys()
print(keys)
print(type(keys))


for key in keys:
    print(key)
    print(mydict[key])



for key in mydict:
    print(key)
    print(mydict[key])
#As same as the first one


leng=len(mydict)
print(leng)