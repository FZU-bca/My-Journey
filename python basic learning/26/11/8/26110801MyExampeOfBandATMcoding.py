money=5000000
name=input("Enter your name:")
def money_checking():
    print(f"{name}, hello, there are {money}$ in your account")
def input_money(x):
    global money
    money=money+x
    print(f"{x}$ have been added")
    print(f"Now you have {money}$ in your account")
def output_money(x):
    global money
    money=money-x
    print(f"{x}$ have been declined")
    print(f"Now you have {money}$ in your account")
def Main_Menu():
    print("-------Main Menu-------")
    print(f"{name}, hello, welcome to the bank ATM")
    print("Check my money, please push'1'")
    print("Add more money, please push'2'")
    print("Decline my money, please push'3'")
    print("Log out, please push'4'")
    Choice=input("Enter your choice:")
    if Choice=="1":
        money_checking()
        print()
        Main_Menu()
    elif Choice=="2":
        add=int(input("Please show how much you want to add:"))
        input_money(add)
        print()
        Main_Menu()
    elif Choice=="3":
        dec=int(input("Please show how much you want to decline:"))
        output_money(dec)
        print()
        Main_Menu()
    else:
        print()
        Main_Menu()
Main_Menu()


