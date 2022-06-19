a = [5, [6], 1, 2, 9, "err", "be"]
b = [[6], 9, 2, 1, "err", "be"]
c = []


for i in a:
    if i in b:
        c.append(i)

print(c)