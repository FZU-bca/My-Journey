#bugs can be conversed
def func1():
    print("function 1 begins")
    num=1/0
    print("function 1 ends")

def func2():
    print("function 2 begins")
    func1()
    print("function 2 ends")

def func3():
    print("function 3 begins")
    try:
        func2()
    except Exception as e:
        print(e)
#This can still run

#To show it more clearly, we want to do not handle the bug and we can clearly see what will happen
def func_1():
    print("function 1 begins")
    num=1/0
    print("function 1 ends")

def func_2():
    print("function 2 begins")
    func_1()
    print("function 2 ends")

def func_3():
    print("function 3 begins")
    func_2()
    print("function 3 ends")

main()