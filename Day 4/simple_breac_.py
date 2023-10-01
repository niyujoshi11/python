av = 10

x = int(input("How many chocolate you want?"))

i = 1
while i <= x:

    if i > av:
        print("Out of stock")
        break

    print("Chocolate")
    i+=1

print("Done")