a = 5
b = 6

temp = a
a = b
b = temp


print(a)
print(b)


a,b = b, a

# second way using xor

# a = a ^ b
# b = a ^ b
# a = a ^ b