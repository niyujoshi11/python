nums = [7,8,9,1,10]
# print(nums[7]) # if we try to print this code the error will return cause there is no index

# for i in nums:
#     print(i)

it = iter(nums)
print(it.__next__())
print(it.__next__())
print(next(it))

# this is iterator demo