#f=open("D:/askdhkjdhkjdas.txt","r",encoding="utf-8")
#This field is not exit
#Then bug happens
#The class told me how to read the error output
#Then he told me how to handle with bug
"""
try:
the codes that might has bug
except
how to run when bug happens
"""
try:
    f=open("D:/askdhkjdhkjdas.txt","r",encoding="utf-8")
except:
    f=open("D:/askdhkjdhkjdas.txt","w",encoding="utf-8")


try:
    print(name)
except NameError as e:
    print("name is not defined")


try:
    1/0
except NameError as e:
    print("name is not defined")
#This can not be successfully runed because the type of naming error is not as same as the fact error

try:
    1/0
    print(name)
except (NameError, ZeroDivisionError) as e:
    print("name is not defined or ZeroDivisionError")

try:
#This type can include all types of bug
    print(name)
except:
#or
    print("name is not defined")
try:
    name = 1/0
except Exception as e:
    #This type can also include all types of bug
    print(name)