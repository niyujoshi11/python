# here is the task that the we have the val that skip while devide by 3 and without 0 remaining
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        continue # continue only skip the execution not the break the loop
    print(i)
print("Done")