Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> {'Имя': "Иван","Фамилия":"Иванов"}
{'Имя': 'Иван', 'Фамилия': 'Иванов'}
>>> a={'Имя': "Иван","Фамилия":"Иванов"}
>>> a
{'Имя': 'Иван', 'Фамилия': 'Иванов'}
>>> a['Имя']
'Иван'
>>> 
>>> a['Имя']='Петр'
>>> a
{'Имя': 'Петр', 'Фамилия': 'Иванов'}
>>> a['Отчество']='Петрович'
>>> a
{'Имя': 'Петр', 'Фамилия': 'Иванов', 'Отчество': 'Петрович'}
>>> a.pop('Имя')
'Петр'
>>> a.