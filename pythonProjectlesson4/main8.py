arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0
pr = 1


for el in arr:
    sum += el
    pr *= el

print("Сумма", sum)
print("Произведение", pr)
