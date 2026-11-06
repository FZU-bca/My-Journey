def add(a,b):
    result= a+b
    return result

r=add(1,2)
print(r)



#if we put a sentence after return, what will happen.
def add(a,b):
    result= a+b
    return result
    print("done")
r= add (1,2)
print(r)

#just as same as break, the sentence after return will not run