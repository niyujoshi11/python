from array import *

arr = array('i',[])

userinput = int(input("Enter the length of your an array:\n"))

for i in range(userinput):
    x = int(input('Enter you next value:\n'))
    arr.append(x)
print("Your array is",arr)

# Now get fetch the value from the user to get it

val = int(input("Enter the value for search for the index:\n"))
kI = 0
for x in arr:
    if x == val:
        # print("Found it.")
        print(kI)
        break
    kI+=1
else:
    print("Not in array.")