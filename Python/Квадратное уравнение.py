import math
#Квадратное уравнение
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=b*b-4*a*c; print('d=',d)

if(d<0):
    print("Корней нет")
elif(d==0):
    print('x=',-b/(2*a))
else:
    x1=int((-b-math.sqrt(d))/2*a)
    x2=int((-b+math.sqrt(d))/2*a)
    print('x1=',x1,'x2=',x2)
