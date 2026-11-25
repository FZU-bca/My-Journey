class Car:
    def __init__(self, c_color, c_brand, c_price):
        self.c_color = c_color
        self.c_brand = c_brand
        self.c_price = c_price
        print("Class finished")
    def running(self):
        print(f"{self.brand}{self.name}running")

    def total_cost(self,discount,rate=0.1):
        total_cost = self.price*discount+rate*self.c_price
        return total_cost

    def __str__(self):
        return f"{self.c_color}{self.c_brand}{self.c_price}"
    def __eq__(self,other):
        return self.c_color==other.c_color and self.c_brand==other.c_brand and self.c_price==other.c_price
    def __lt__(self,other):
        return self.c_price<other.c_price

#tring
c1=Car("red",'BMW','100000000')
print(c1)
c2=Car("red",'BMW','100000000')
print(c2)

print(c1==c2)
print(c1<c2)
print(c1>c1)


