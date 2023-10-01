# end="" is used for the skiping the new line
# print("# ", end="")
# print("# ", end="")
# print("# ", end="")
# print("# ", end="")
# print("we are done")

# new patterns

#  Method 1
# for j in range(4):
#     print("# ", end="")
# print()
# for j in range(4):
#     print("# ", end="")

# Method 2

for i in range(4):
    for j in range(4):
        print("# ", end="")
    print()
    