# strings are immutable in python
# String Demo
print("nihir's " "Laptop")

a = "youtube"
print(a)

b = a[:3]  # output will be "yout"
b = a[3:4] # output will be "tu"
b = a[-1:] # output will be "e"
print(b)


newname = "My" + a[3:]
print(newname)

# for getting the length of string len

print(len(newname))