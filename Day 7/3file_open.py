# for readinig
f = open("readme.md", 'r')

text = f.read()
print(text)

f.close()

# for writing
w = open("readme.md",'w')
w.write("Hehehe")

w.close()