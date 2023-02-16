Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1, 2, 2.5, '(QWR)', 3, 4, 5]
>>> 
>>> 1
1
>>> l
[1, 2, 2.5, '(QWR)', 3, 4, 5]
>>> type(l)
<class 'list'>
>>> len(l)
7
>>> l[5]
4
>>> 1[3]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    1[3]
TypeError: 'int' object is not subscriptable
>>> l=[1, 2, 2.5, '(QWR)', 3, 4, 5]
>>> l
[1, 2, 2.5, '(QWR)', 3, 4, 5]
>>> l=l=[1, 2, 2.5, 'QWR', 3, 4, 5]
>>> l
[1, 2, 2.5, 'QWR', 3, 4, 5]
>>> l[3]
'QWR'
>>> l[3]+'RR'
'QWRRR'
>>> (1[3], ' ')*10
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    (1[3], ' ')*10
TypeError: 'int' object is not subscriptable
>>> (1[3] + ' ')*10
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    (1[3] + ' ')*10
TypeError: 'int' object is not subscriptable
>>> ll=[0]
>>> l+ll
[1, 2, 2.5, 'QWR', 3, 4, 5, 0]
>>> ll*5
[0, 0, 0, 0, 0]
>>> 1[3]*10
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    1[3]*10
TypeError: 'int' object is not subscriptable
>>> s='sdfghjkl'
>>> ll*0
[]
>>> (l[3] + ' ')*5
'QWR QWR QWR QWR QWR '
>>> ll*-1
[]
>>> s[2:5]
'fgh'
>>> len(s)
8
>>> s[0:11]
'sdfghjkl'
>>> s[0:12]
'sdfghjkl'
>>> s[0:11:2]
'sfhk'
>>> s[5]
'j'
>>> s[:5}
SyntaxError: invalid syntax
>>> s[:5]
'sdfgh'
>>> s[5:]
'jkl'
>>> s[:]
'sdfghjkl'
>>> s
'sdfghjkl'
>>> s[::-1]
'lkjhgfds'
>>> s[::-2]
'ljgd'
>>> s[::-5]
'lf'
>>> s[::0]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s[::0]
ValueError: slice step cannot be zero
>>> s[::]
'sdfghjkl'
>>> s[-3]
'j'
>>> s[-3:]
'jkl'
>>> s[-3:3]
''
>>> s[-3:3:-1]
'jh'
>>> n=[игра]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    n=[игра]
NameError: name 'игра' is not defined
>>> n="игра"
>>> n
'игра'
>>> m="гора"
>>> m
'гора'
>>> c=n[0:2]+m[0:2]*2
>>> c
'иггого'
>>> c=n[0:1]+m[0:2]*2
>>> c
'игого'
>>> c=n[0:2]+m[0:2]*2
>>> l1='игра';l2='гора';l=ll[0]+l2[:2]*2
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    l1='игра';l2='гора';l=ll[0]+l2[:2]*2
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 3>5
False
>>> type(3>5)
<class 'bool'>
>>> a="огого"
>>> a==a*-1
False
>>> a*(-1)
''
>>> a=a[::-1]
>>> a==a[::-1]
True
>>> a[0]='W'
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a[0]='W'
TypeError: 'str' object does not support item assignment
>>> 