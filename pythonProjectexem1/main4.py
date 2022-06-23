inp_0 = str(input('Введите последовательность :'))
inp_0 = list(inp_0)

inp_1 = str(input('Какую цифру будем искать?'))

count = 0

for i in inp_0:
    if i == str(inp_1):
        count += 1

print(count, inp_1)
