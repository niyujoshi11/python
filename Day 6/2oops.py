# object creation

class Computer1:
    # the init function called automatically
    def __init__(self, cpu, ram ) -> None: # in general is using for the initialize varibale for the project 
        self.cpu = cpu # you can use different varibale name as well
        self.ram = ram # you can use different varibale name as well

    def config(self):
        print("The system configuration ram is ",self.ram, "& cpu is ",self.cpu)


# comp1 = Computer("i5",12)
# comp1 = Computer.config(5, 'i3')
# Computer.configuration("i5",12 )

class Computer:
    def __init__(self,ram,cpu):
        self.ram = ram
        self.cpu = cpu
    
    def config(self):
        print("Config is",self.ram, self.cpu)

com1 = Computer('i4', 12)
com2 = Computer('AMD', 18)

com1.config()
com2.config()