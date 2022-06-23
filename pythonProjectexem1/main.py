a = str(input("введите семизначное число: "))
even = 0
odd = 0
sum = 0
pr = 1
for i in a:
    if int(i) % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

if even > odd:
    for i in a:
        sum = sum + int(i)
    print(sum)

else:
    for i in list(a):
        pr = pr * int(a[0]) * int(a[2]) * int(a[5])
    print(pr)