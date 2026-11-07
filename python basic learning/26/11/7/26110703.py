# def test_A():
#     num=100
#     print(num)
#
#
# test_A()
# print(num)
#error happens because the "num" is defined in the function and not at the outside, so the error is name is not defined



# num = 100
# def test_B():
#     print(num)
#
#
#
# def test_C():
#     print(num)
#
# test_B()
# test_C()
# print(num)

#
#
# num = 100
# def test_B():
#     print(num)
#
#
#
# def test_C():
#     num=500
#     print(num)
#
# test_B()
# test_C()
# print(num)



num = 100
def test_B():
    print(num)



def test_C():
    global num
    num=500
    print(num)


    
def test_D():
    print(num)

test_B()
test_C()
test_D()
print(num)






