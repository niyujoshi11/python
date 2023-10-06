# Here in the deep down to init & contruct

class Computer:
    def __init__(self):
        self.name = "Nihir"
        self.age = 21

    def update(self):
        self.age = 23

    def compare(self,other):
        if(self.age) == other.age:
            return True
        else:
            return False
        
c1 = Computer()
c2 = Computer()

c2.name = "New Name"
c2.age = 23

# Compare 
if c1.compare(c2):
    print("Both are same")
else:
    print("Both are not same")

c2.update()

print(c1.name)
print(c2.name)