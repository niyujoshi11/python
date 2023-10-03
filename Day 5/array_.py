# for using array you have to import it
# in array all values should have same type so that you have to define the type
# if you use first method then you have to use like this
# import array
# val = array.array()
# or you can use 
from array import *
vals = array('i',[1,2,3,4,5])
print(type(vals)) # this is the type of an array
print(vals.buffer_info()) # buffer info is used for getting the information about it the first is address of the array & the second is the parameter size

# array is similar to list so you can use the all list sub functions & more
