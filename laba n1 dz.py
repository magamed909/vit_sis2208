import math
print("Введите коэффициенты уравнения")
print("a = ", end ='')
a = float(input())
print("b = ", end = '')
b = float(input())
print("c = ",end = '')
c = float(input())
D = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % D)
if D > 0:
    x1 = (-b + math.sqrt(D))/(2 * a)
    x2 = (-b - math.sqrt(D))/(2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif D == 0:
    x = -b/(2 * a)
    print('x = %.2f' % x)
else:
    print('Корней нет')
