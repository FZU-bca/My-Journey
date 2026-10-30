#if
print("Welcome, just play for free, but please enter your age first")
age=int(input("Enter your age:"))

if age>=18:
    print(f"You are old enough, so please first pay for 30$ before playing.")
if age<18:
    print("you are not old enough, so just pay for 10$.")

print("Enjoy your time!!!")



#if else
print("Welcome again")
age=int(input("Enter your age:"))
if age>=18 :
    print(f"You are old enough, so please first pay for 30$ before playing.")
else :
    print("You are not old enough, so just pay for 10$.")
print("Enjoy your time!!!")


#if elif else
print("Welcome again")
height=int(input("Enter your height:(cm)"))
vip_level=int(input("Enter your vip level:（1-5）"))
day=int(input("Please tell me what the date today:"))
if height<=120:
    print("Your height is less than 120cm, so you can play freely")
elif vip_level>=3:
    print("Because you are our vip custom, so you can play freely")
elif day==15 or day==30 or day==1:
    print("Today is our free day, and you do not need to pay anything.")
else:
    print("Sorry, you are taller than 120cm, and you are not our vip custom, so pay for 10$ if you want to conti.")
print("Enjoy your time!!!")
"""if condition will check the input one by one. for e.x. if your height is smaller than 120, and the condition next will not be changed.
if the height is 160, the vip_level=3, finally the condition of date will not be checked so as print sentence.
"""

#simplify
print("Welcome again")
if int(input("Enter your height:(cm)"))<=120:
    print("Your height is less than 120cm, so you can play freely")
elif int(input("Enter your vip level:（1-5）"))>=3:
    print("Because you are our vip custom, so you can play freely")
elif int(input("Please tell me what the date today:"))==15 or int(input("Please tell me what the date today:"))==30 or int(input("Please tell me what the date today:"))==1:
    print("Today is our free day, and you do not need to pay anything.")
else:
    print("Sorry, you are taller than 120cm, and you are not our vip custom, so pay for 10$ if you want to conti.")
print("Enjoy your time!!!")
#but this term is not easy to read I think

#practice
print("Let's play a game, and you will have 2 chances")
num=int(input("Enter your number:"))
if num==10:
    print("Congratulations, you get the correct answer ")
elif num!=10:
    print("Sorry,the answer isn't correct and you only have one last chance")
elif num==10:
    print("Congratulations, you get the correct answer ")
else:
    print("Sorry, the answer isn't correct.")
print("Do you want to play again?")
#It is not necessary to list the "!=",because when the right condition is checked one by one and if the num is not correct whole time, then the else condition will be checked and output will be False because the condition ahead are checked.



#Better solution
num=10

if int(input("Enter your first guess:"))==num:
    print("Congratulations, you get the correct answer ")
elif int(input("No, it is not the correct number.Enter your second guess:"))==num:
    print("Congratulations, you get the correct answer ")
elif int(input("No, it is not the correct number.Enter your third guess:"))==num:
    print("Congratulations, you get the correct answer ")
else:
    print("Sorry, game over~~~.")
print("Do you want to play again?")






