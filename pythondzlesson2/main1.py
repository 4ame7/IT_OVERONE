a = int(input('a = '))
b = int(input('b ='))
c = int(input('c = '))

if a + b < c or a + c < b or b + c < a:
    print("Треугольник не существует")
elif a != b and b != c and a != c:
    print("Разносторонний")
elif a == b and b == c and a == c:
    print("Равносторонний")
else:
    print("Равнобедренный")