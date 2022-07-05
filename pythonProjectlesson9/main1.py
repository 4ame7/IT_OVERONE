import random

a = ([random.randint(0, 5) for _ in range(10)])
b = ([random.randint(-5, 0) for _ in range(10)])

c = a + b
print(c, '\n Количество нулей: ', c.count(0))