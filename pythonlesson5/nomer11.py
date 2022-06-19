print("Ноль в качестве знака операции прекращает работу программы")

a = float(input("a="))
b = float(input("b="))

while True:
    s = input("Знак (+, -, *, /): ")

    if s == 0:
        break
    elif s == "+":
        print(a + b)
    elif s == "-":
        print(a - b)
    elif s == "*":
        print(a * b)
    elif s == "/":
        if b != 0:
            print(a / b)
        else:
            print("Деление на ноль")