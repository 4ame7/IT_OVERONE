year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('Год является високосным')
else:
    print('Год не является високосным')