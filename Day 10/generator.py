# there is minor difference between function & generators if you return the value it will simple function & if you yield value like itrator then that function will work like generators
# def geneRator():
#     yield  1
#     yield  2
#     yield  3
#     yield  4

# values  = geneRator()

# print(values.__next__())

# for i in values:
#     print(i)

def topten():
    n = 1

    while n <= 10:
        sq = n*n
        yield sq
        n += 1

values  = topten()


for i in values:
    print(i)