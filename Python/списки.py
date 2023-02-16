def mysqr(x):
    return x*x
l=list(map(float,input("Введите элементы списка через пробел: ").split()))

#print(l[::-1])
#print(l.reverse())

ll=[]
for x in l:
    ll.append(mysqr(x))

print("-Первый способ---", ll)
print("--Второй способ--", list(map(mysqr, l)))
print("---Третий способ-", list(map(lambda x: x*x, l)))




print("-"*3, "*", "-"*3)                                     
print("-"*2, "*"*3, "-"*2)
