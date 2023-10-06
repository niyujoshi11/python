class Bike:
    wheels = 2 # Class variable 
    def __init__(self):
        self.mil = 10 # initial global variable or intance varibale
        self.com = "KTM"
    
b1 = Bike()
b2 = Bike()

b1.mil = 50
b1.com = "splendar"

Bike.wheels = 3 # Here i can change the value of class global varibale or the namespace

print(b1.com, b1.mil, b1.wheels)
print(b2.com, b2.mil, b2.wheels)