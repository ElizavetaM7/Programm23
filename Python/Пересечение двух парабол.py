from math import *
#Функция для решения линейного уравнения ax+b=0
def lin_eq(a,b):
    if a!=0:
        return -b/a
    elif b==0:
        return 'x - любое'
    else:
        return 'Решений нет'

#Функция для решения квадратного уравнения ax^2+bx+с=0
def sqr_eq(a,b,c):
        if a==0:
            return lin_eq(b,c)
        else:
            D=b*b-4*a*c
            if D<0:
                return 'Решений нет'
            elif D==0:
                return -b/2/a #Или -b/(2*a) - то же самое
            else:
                x1=(-b-sqrt(D))/(2*a)
                x2=(-b+sqrt(D))/(2*a)
                return [x1,x2]

#Основная программа
print('Проверка пересечения двух парабол')
print('Введите коэффиценты первой параболы')
a1=float(input('a = '))
b1=float(input('b = '))
c1=float(input('c = '))
print('Введите коэффиценты второй параболы')
a2=float(input('a = '))
b2=float(input('b = '))
c2=float(input('c = '))

res=sqr_eq((a2-a1), (b2-b1), (c2-c1))

if isinstance(res, list):
    print("Две точки пересечения")
elif isinstance(res, float):
    print("Одна точка пересечения")
elif res=='решений нет':
    print('Параболы не пересекаются')
else:
    print('Параболы совпадают')

print(sqr_eq((a2-a1), (b2-b1), (c2-c1)))
