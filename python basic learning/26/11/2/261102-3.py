i=1
while i<=100:
    print(f"Today is the {i} day, ready to say 'I love you' to her")
    j=0
    while j<10:
        print(f"Give her the {j} flower")
        j+=j+1
    print("I love you")
    i += 1
print(f"Until day {i}, success")



#There is a little problem in it, and the final output is that: Until day 101,success.But the answer we want is :Until day 10,success.The reason is that when i=100, i will walk that road again(i+=1)

i=0
while i<=100:
    print(f"Today is the {i} day, ready to say 'I love you' to her")
    j=0
    while j<10:
        i+=1
        print(f"Give her the {j} flower")
        j+=j+1
    print("I love you")
print(f"Until day {i}, success")


#But when we put "i+=1"to the top of while sentence and the initial value of i equals to 0, the problem is solved