def test_function(compute):
    result=compute(1,2)
    print(type(compute))
    print(result)

def compute(x,y):
    return x+y
test_function(compute)