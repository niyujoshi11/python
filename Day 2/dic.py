# In Python, dictionaries are written with curly brackets { } , 
# and store key-value pairs. Dictionary keys should be the immutable Python object, 
# for example, number, string, or tuple. Keys are case sensitive. Duplicate keys are not allowed in the dictionary
# mutable
data = {0:0, 1:"Nihir", 2:"Zala", 3:"Test"}

# data uses index key
data[1]

data.get(4, "Not got it, Create one")

keys = ["Dell", "Nihir", "Tesst"]
values = ["System", "Zala", "Here"]

newdata = dict(zip(keys,values))

data["Dell"]

# for added the new list
data["newadd"] = "val-here"

del data["newadd"]

# Dic in dic

pro = {'js':'atom', 'cs':'vs', 'python':['pycharm','sublime'], 'java':{'jse':'netbeans','jee':'eclips'}}

print(pro)
print(pro["cs"])
print(pro["python"][1])
print(pro["python"])