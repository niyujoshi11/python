# all class have attributes & behaviors
# attributes is are variables
# behaviour is method(Functions)
# to define a class you have to mention that class className like here.

class ClassName:
    def funName():
        print('HeLlo word')
    

class Computers:
    def config(self): # self is generally worked like the construct function
        print("This is HP laptop with the 12 gb Ram")

class Laptop:
    def config(self):
        print("THis is the laptop")

lenovo = Computers()
dell = Laptop()

Computers.config() # do not call like this if it takes parameters
# print(type(comp1))

# to call the function from the class you have to first call the class then function

# ClassName.funName(comp1)
Computers.config(lenovo) # you can define like this
Laptop.config(dell)

lenovo.config() # you can define like this also