class Student:
    def __init__(self,m1,m2):
        self.m1 = m1 # marks 1
        self.m2 = m2 # marks 2
    
    def sum(self,a=None,b=None,c=None): # if you print the value as it is & accepting only 2 value you will get the error for solving that you have to set default as null
        s=0
        if a!= None and b!=None and c!=None:
            s = a+b+c
        elif a!= None and b!=None:
            s = a+b
        else:
            s=a
        return s

    
s1 = Student(58,56)
print(s1.sum(5,9,6))