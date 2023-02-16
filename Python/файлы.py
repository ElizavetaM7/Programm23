
##lst=[x**3 for x in range(1,6) if x%2==1]
##f=open('test-1.txt', 'w')
##
##
##for l in lst:
##    f.write(str(l)+'\n')
##
##f.close()

##with open('test-1.txt', 'w') as f:
##    for l in lst:
##        f.write(str(l)+'\n')
##print('ok')


##with open('test-1.txt', 'r') as f:
##   x=f.readlines()
##
##x=[a.rstrip for a in x]
##print(x)
##print('ok')


##with open ('Дата.csv', 'r') as f:
##    data=f.readlines()
##
##d=[]
##for x in data:
##    d.append(x.strip().split(',')) #strip() - удаление нечитаемых символов
##print(d[2],[2])


##with open ('Дата.csv', 'r') as f:
##    while(True):
##        data=f.readlines()

##print('    *')
##print('    -')
##print('   - -')
##print('  - - -')
##print(' - - - -')
##print('- - - - -')


##Третий спооб - Только для .CSV_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
import csv

##with open ('Дата.csv', 'r') as f:
##    reader=csv.reader(f)
##    for x in reader:
##        print(x)
##    


with open ('cvcb.csv') as f:
    reader = csv.reader(f,delimiter=';')
    data=[]
    for x in reader:
        data.append(x)

s1=0;
s2=0;
s3=0;
for i in data:
    s1+=int(i[0])
    s2+=int(i[1])
    s3+=int(i[2])
print(s1, s2, s3)

    






       
