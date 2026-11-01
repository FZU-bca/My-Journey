print("Welcome to the zoo!")
if int(input("Please enter your height:")) > 120:
    print("Because your height is more than 120, so you can not view for free")
    print("But if your VIP_Level is more than3,you can view for free")

    if int(input("Please tell me your VIP_Level:")) > 3:
        print("Thank you and you can view for free")
    else:
        print("Sorry, you need to pay for 10$")
else:
    print("Welcome little friend and you can view for free")