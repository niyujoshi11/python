nums = [9,11,12,13,14,6]

# Method 1\

for i in nums:
    if i%5 == 0 :
        print(i)
        break # I only want it one time
    # else:
        # print("Not found") # this will print 5 times
else:
    print("Not found")