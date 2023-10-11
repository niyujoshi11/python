# 1 + 2 are operands
# + is operators

a = 2
b = 3

print(a+b)

int.__add__(a,b) 

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1 # marks 1
        self.m2 = m2 # marks 2
    
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3



s1 = Student(50,49)
s2 = Student(45,40)

# s3 = s1 + s2  # if you try to run this code you will get the error the code works behind Student.__add__(s1,s2)

# for that you have run the add function
s3 = s1 + s2
print(s3)
print(s3.m1)
print(s3.m2)