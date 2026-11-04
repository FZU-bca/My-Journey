for i in range(5):
    print(i)
print(i)
#A special form of "range", can run but not commanded, and hopefully not use this form
#solution
i=0
for i in range(5):
    print(i)

print(i)
#same as the rule but not useful enough


#new knowledge:
#Say hello to Mei 100 days and every day give her a flower
i=0
for i in range(0,101):
    print(f"Hello Mei,today is the {i} I meet you")
    for n in range(0,11):
        print("Give her a flower")
print("I love you")
print("")
print(".........")
print("")
print("So do I")


#with the use of both "while" and "for"
i=1
while i<=100:
    print(f"Hello Mei,today is the {i} I meet you")
    j=0
    for j in range(0,11):
        print("Give her a flower")
    i+=1
print(f"This is the {i-1} day that I meet you, and what I want to say is I love you")
