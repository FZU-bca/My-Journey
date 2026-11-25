class Car:
    wheel=4
    tax_rate=0.1
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.c_color = c_color
        self.c_brand = c_brand
        self.c_name = c_name
        self.c_price = c_price
        self.wheel = 2#This will change the total class index
    def running(self):
        print(self.c_color,self.c_brand,self.c_name,self.c_price)
    def total_price(self,discount,rate=0.1):
        total_price = discount * self.c_price + rate * self.c_brand
        return total_price

c1=Car('red','BYD','c100',1000000)
c2=Car('green','BDG','c200',1000000)
print(c1)
print(c2)
print(c1.c_brand)
print(c1.wheel)
print(Car.wheel)