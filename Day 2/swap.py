a = 5
b = 6

tempVar = a
a = b
b = tempVar


print(a)
print(b)

a, b = b, a

20, 30 = 30, 20

# second way using xor

# a = a ^ b
# b = a ^ b
# a = a ^ b