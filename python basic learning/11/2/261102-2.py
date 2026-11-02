i=0
while i<100:
    print("ysw love jsy")
    i+=1
if i==100:
    print("jsy love ysw")


num=1
total=0
while num<=100:
    total=total+num
    num=num+1
print(total)


import random
N=random.randint(1,100)
G=int(input("Guess the number"))
A=1
while G!=N:
    if G>N:
        print("Too high")
    else:
        print("Too low")
    G=int(input("Guess the number again"))
    A=A+1
print(f"You guessed the number, and you guessed {A}times")


