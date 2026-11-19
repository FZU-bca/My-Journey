#How to make a Module by my self
def test(a,b):
    print(a+b)
#and now we can use this Module in another program, which the action is as same as what I have learned before
#the name of Module is the name of program which will be seen as Module

#But there another example that need to be noticed
#The code in Module1:
"""
def my_text(a,b):
print(a+b)
"""
#The code in Module2:
"""
def my_text(a,b):
print(a-b)
"""
#and the result is that the last one will cover all functions before
#That is Module2 will be runed


#if we run function in Module even if we only import the Module the run function will be runed
#here is a solution
"""
if __name__ == "__main__":
text(1,2)
in this way this will not be runed even be imported
"""
__all__=["textA"]
def textA(a,b):
    print(a+b)
def textB(a,b):
    print(a-b)

#in another program when we use '*' textB is not included
#but if we have defined name we can still use textB