stroka = 'Hello, my, friend, how, are, you'
a = tuple(str(item) for item in stroka.split(','))
c = (''.join(a))
print(c)