#the using of knowledge that I have learned before
#write a program for salary giving



#the way I chose
money=10000
i=0
for i in range(1,21):
    import random
    score = random.randint(1,11)
    if money <= 0:
        print("Sorry because we do not have enough money so we do not have enough money to give you your salary")
    else:
        if score < 5:
            print("Because you do not have enough score so you can not have your salary")
        else:
            print("Well done in this mouth and we will give you your salary")
            money = money-1000


#The way that example give
for i in range(1,21):
    import random
    score = random.randint(1,11)


    if score < 5:
        print(f"Because you do not have enough score so you can not have your salary")
        continue

    if money>=1000:
        money -=1000
        print("Because you  have enough score so you can have your salary")
    else:
        print("Because we do not have enough money so you can not have your salary")
        break