#Overview about list
mylist = [1,2,3,4,5,6,7,8,9]
def list_while_func():
    index = 0
    while index < len(mylist):
        number = (mylist[index])
        print(number)
        index += 1
list_while_func()


def list_for_func():
    for element in mylist:
        print(element)

