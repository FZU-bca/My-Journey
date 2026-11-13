def test_return():
    return 1,"Hello",True
x,y,z=test_return()
print(x)
print(y)
print(z)
def user_info(name,age,gender):
    print(f"Your name is {name}, age is {age}, gender is {gender}")


user_info('Tim',18,"M")
user_info(name='Tim',gender='M',age=18)
def user_inro1(name,age,gender='M'):
    print(name,age,gender)
user_inro1('Tim',18)


def user_inro2(*args):
    print(args)
user_inro2('Tim',18)
user_inro2('Tim',18,'M')



def user_inro3(**kwargs):
    print(kwargs)


user_inro3(name='Tim',age=18)
user_inro3(name='Tim',age=18,gender='M')