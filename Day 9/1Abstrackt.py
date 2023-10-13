# when you pass the pass in method which have nothing to return than your method called abstract method


from abc import ABC,abstractclassmethod

class Computer(ABC):
    @abstractclassmethod
    def process(self):
        pass
        # print("Running")


class Laptop(Computer):
    # pass
    def process(self):
        print("New running")


class Program:
    def work(self):
        print("Hello Programmer")


# com =Computer()
# com.process()
# com1 = Laptop()
# com1.process()
com2 = Program()
com2.work()