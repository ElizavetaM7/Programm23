a="зима"
b="лето"
S=""
for i in range(0,len(a)):
    S=S+a[i]+b[i]
print(S)

st="программирование"
print(st.find("грамм"))
L=st.split("мм")
print(L)
print("мм".join(L))
L1=[1,2,3]
L2=["z","x","cvb"]
#r1=L1.append(4)
#print(r1)
#r1=L1.append(12)
#print(r1)

L=[[1,2,3],[4,5],[9,8,7,6]]
resL=[]
for x in L:
    resL.extend(x)
print(resL)

print("--------------------------------------------------------------------")
t=0
while t>0:
    t=t-1
    print(t)
else:
    print(":(")

print("--------------------------------------------------------------------")
def my_sqr(t):
    return t*10

k=[97,98,99, "axax"]
for x in k:
    print (my_sqr(x))
    
