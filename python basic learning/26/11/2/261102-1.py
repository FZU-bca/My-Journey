import random
num = random.randint(1,10)
num_guess = int(input("Please tell me the first number you guess, and you have three chances"))
if num_guess == num:
    print("You guessed the number")
elif num_guess < num:
    print("Too low, try again")
    num_guess = int(input("Please tell me your number, and you have two chances now"))
    if num_guess == num:
        print("You guessed the number")

    elif num_guess < num:
        print("Too low, try again")
        num_guess = int(input("Please tell me your number, and you have one chance now"))
        if num_guess == num:
            print("You guessed the number")
        elif num_guess < num:
            print(f"Too low, and the answer is {num}")
        else:
            print("Too high, and the answer is {num}")

    else:
        print("Too high, try again")
        num_guess = int(input("Please tell me your number, and you have one chance now"))
        if num_guess == num:
            print("You guessed the number")
        elif num_guess < num:
            print("too low, and the answer is {num}")
        else:
            print("too high, and the answer is {num}")
else :
    print("Too high")
    num_guess = int(input("Please tell me your number, and you have two chances now"))
    if num_guess == num:
        print("You guessed the number")
    elif num_guess < num:
        print("Too low, try again")
        num_guess = int(input("Please tell me your number, and you have one chance now"))
        if num_guess == num:
            print("You guessed the number")
        elif num_guess < num:
            print("too low, and the answer is {num}")
        else:
            print("too high, and the answer is {num}")
    else:
        print("Too high, try again")
        num_guess = int(input("Please tell me your number, and you have one chance now"))
        if num_guess == num:
            print("You guessed the number")
        elif num_guess < num:
            print("too low, and the answer is {num}")
        else:
            print("too high, and the answer is {num}")