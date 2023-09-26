# list uses sqare brackets

nums = [10, 12, 13, 14, 15]
print(nums)

print(nums[0])
print(nums[1])
print(nums[4])

names = ["Nihir", "Zala", "Test"]
print(names)

mix = [nums, names]
print(mix)

append = nums.append(55)
print(nums)

insert = nums.insert(3, 66)
print(nums)

remove = nums.remove(14)
print(14)

pop = nums.pop(2)   # it uses from index number
print(nums)

pop = nums.pop()   # it uses from last index number
print(nums)

del nums[2:5]  # used for this elements
print(nums)

# for add multiple values
nums.extend([111, 222, 333])

print(nums)

min(nums)
max(nums)
sum(nums)

nums.sort() # for sorting list