name="114514"
length = len(name)
print(length)

#how to create a function (the first step)
str1="114514"
str2="341125"
str3="4949849694"

count=0
for i in str1:
    count+=1
print(count)


#how to definite a function to create a diy function and simplify the code, very easy brief and useful
def my_len(data):
    count=0
    for i in data:
        count += 1
    print(f"the length of {data} is {count}")


my_len(str1)
my_len(str2)
my_len(str3)




