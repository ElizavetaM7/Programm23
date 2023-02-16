s1=list(map(float, input("Введите элементы первого списка через пробел: ").split()))
s2=list(map(float, input("Введите элементы второго списка через пробел: ").split()))
maxS=[]
for i in range(0,len(s1)):
    M=max(s1[i], s2[i])
    maxS.append(M)
print(maxS)
