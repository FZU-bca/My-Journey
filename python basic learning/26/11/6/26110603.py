#"none" means nothing meaningful is returned
#a new type called NoneType
#none ==meaningless
def say_hi():
    print("Hello")

result=say_hi()
print(result)
print(type(result))



def say_hi2():
    print("Hello")
    return None
result=say_hi2()
print(result)
print(type(result))



#none can be used in if sentence
def check_age(age):
    if age>18:
        return "SUCCESS"
    else:
        return None

result=check_age(16)
if not result:
    print("you are too young")

