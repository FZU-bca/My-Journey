i=range(5)
print(i)
a=range(2,10)
print(a)
b=range(1,11,2)
print(b)
#But it just directly print "range(i)", but I want to print the form like{0,1,2,3,4}
#Finally AI told me that range is a type of list so we can write"print(list(x))" to print out all ranges.
print(list(i))
print(list(a))
print(list(b))

#most of "range" appeared with "for"
for x in range(5):
    print(x)
print()
for i in range(5,16):
    print(i)
print()
for a in range(5,16,3):
    print(a)

#show a example that I have written before with "while"
#and in the same time, I can use for+range to make it come ture
i=1
while i<=10:
    print("Give flower")
    i+=1


for x in range(10):
    print("Give flower")
