# Here in the deep down to init & contruct

class Computer:
    def __init__(self):
        self.name = "Nihir"
        self.age = 21

    def update(self):
        self.age = 23


c1 = Computer()
c2 = Computer()

# c2.name = "New Name"
# c2.age = 23

c2.update()

print(c1.name)
print(c2.name)