nums = [10,11,12,13,14,15]

# Method 1\

for i in nums:
    if nums%5 == 0 :
        print(nums)
        break # I only want it one time
    # else:
        # print("Not found") # this will print 5 times
else:
    print("Not found")