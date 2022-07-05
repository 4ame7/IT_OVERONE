stroka = input("Напишите предложение с знаками препинания :")
a = tuple(str(item) for item in stroka.split(','))
c = (''.join(a))
print(c)