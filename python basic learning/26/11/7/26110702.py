def func_b():
    print("---3---")

def func_a():
    print("---1---")
    func_b()
    print("---2---")

func_a()
#The understanding of function in function