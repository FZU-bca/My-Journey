class Car:#The name of class must as same as JAVA's method for example:SuperMarket
    pass
c1=Car()
c1.brand="BMW"
c1.name="X5"
c1.color="red"
c1.price=500000
print(c1.__dict__)#Means that the information will be stored in dictionary
print(c1)
print(c1.name)
print(c1.price)
print(c1.brand)
#This not the best way to define a class
class Car:
    def __init__(self,c_brand,c_name,c_price):
        self.c_brand=c_brand
        self.c_name=c_name
        self.c_price=c_price
car2=Car("BMW","X5",500000)
print(car2.__dict__)
print(car2)
#This method is the most useful way to make a project




