import math


AB = input("Длинна первого катета")
AC = input("Длинна второго катета")


AB = float(AB)
AC = float(AC)

BC = math.sqrt(AB**2 + AC**2)

S = (AB * AC) / 2

P = (AB + AC + BC)

print(S)
print(P)
