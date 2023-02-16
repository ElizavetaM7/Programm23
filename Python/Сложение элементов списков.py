from math import sqrt

list1=list(map(float,input("Введите первый список: ").split()))
list2=list(map(float,input("Введите второй список: ").split()))
reslist=[]

for i in range(len(list1)):
    reslist.append(list1[i]+list2[i])

print(reslist)
print(list(map(sqrt, reslist)))
