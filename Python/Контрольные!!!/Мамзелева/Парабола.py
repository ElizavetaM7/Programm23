import math
a1=int(input())
b1=int(input())
c1=int(input())
a2=int(input())
b2=int(input())
c2=int(input())


A=a1-a2
B=b1-b2
C=c1-c2
D=(B**2)-4*A*C


if(D<0):
    print("Нет решения->нет пересечений")
elif(D==0):
    X1=((-B)/(2*A))
    print("Одна точка пересечения", X1)
else:
    X1=((-B+math.sqrt(D))/(2*A))
    X2=((-B-math.sqrt(D))/(2*A))
    print("Две точки пересечения", X1, X2)

    
