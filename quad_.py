import math

a = int(input("Введите значение А "))
b = int(input("Введите значение B "))
c = int(input("Введите значение C "))
D = (b**2) - 4*a*c
if D < 0:
    print("уравнение не имеет корней!")
elif D == 0:
    print(f"Корень уравнения равен {-b+(math.sqrt(D)/2*a)}")
elif D > 0:
    print(f"Корень уравнения № 1 равен {-b + (math.sqrt(D) / 2 * a)}")
    print(f"Корень уравнения № 2 равен {-b - (math.sqrt(D) / 2 * a)}")
