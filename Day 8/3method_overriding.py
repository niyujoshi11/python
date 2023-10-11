class A:
    def show(self):
        print("in a show")
class B(A): # here i inherit the class A so that B can uses all functions of Class A
    pass



# a1 = A()
# a1.show()
b1 = B()
b1.show()