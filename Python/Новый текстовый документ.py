from tkinter import *
from tkinter.ttk import *
import csv

wnd=Tk()
wnd.geometry('800x600+300+100')
tv=Treeview(columns=['1','2'])
tv.heading('#0', text='Фамилия')
tv.heading('#1', text='Имя')
tv.heading('#2', text='Отчество')



with open ('Дата.csv') as f:
    data=[]
    reader = csv.reader(f,delimiter=';')
    for x in reader:
        data.append(x)

for d in data:
    tv.insert('',END, text=d[0],values=d[1:])

tv.pack(expand='True', fill='both')

mainloop.wnd()
