a = 5
b = 0

try:
    print(a/b)
except Exception:
    print("Can not work this perform")
print("Process done")

# if you want to an error which is it than add as e
try:
    print(a/b)
except Exception as e:
    print("Can not work this perform",e)
finally:
    print("This will return as it is whether your condtion is true or false or anything this will return")
print("Process done")