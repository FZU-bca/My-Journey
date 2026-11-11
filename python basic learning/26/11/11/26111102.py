#Method 1
mylist="12313noitcanakaS3111"
mylove=mylist[15:4:-1]
print(mylove)
#Method 2
mystring_1=mylist[::-1][4:15]
print(mystring_1)
#Method 3
mystring_2=mylist[5:16][::-1]
print(mystring_2)
#Method 4
mystring_3=mylist.split("3")
mystring_4=mystring_3[2][::-1]
print(mystring_4)