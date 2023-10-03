# to define the function you have to use the keywork called def

def test1():
    print("Hello Theree")
    additions()


def additions(): 
    x = int(input("Enter x value:\n"))
    y = int(input("Enter y value:\n"))
    c = x + y
    print("The addition of the value which you entered is ",c)

test1()
# additions()

# you can add the params like this

def test(a="Hello"):
    print(a)