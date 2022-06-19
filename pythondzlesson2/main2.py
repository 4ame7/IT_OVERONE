import math

print("Введите координаты точки и радиус круга")
x_point = float(input("x = "))
y_point = float(input("y = "))
radius = float(input("r = "))

hypotenuse = math.sqrt(x_point**2 + y_point**2)
if hypotenuse <= radius:
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")