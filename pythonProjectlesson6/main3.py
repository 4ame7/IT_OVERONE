a = [4,6,"pe",45,293]
b = ["tr",24,45,1]
a.extend(b)
a.insert(3,6)
print(a)
for i in a:
    if type(i) is str:
        a.remove(i)
a.sort()
print(a)