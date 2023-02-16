from tkinter import *
import tkinter.messagebox

def myFunc(event):
    a=len(set(ent_01.get()) & set(ent_02.get()))
    
    b=tkinter.messagebox.showinfo(message='Имеется '+str(a)+' одинаковых буквы')

myApp=Tk()
myApp.title("Слово в слове")
myApp.geometry('400x100+250+150')


lbl_01=Label(text='Первое слово: ',font='Arial 12 bold')
lbl_02=Label(text='Второе слово: ',font='Arial 12 bold')
ent_01=Entry(font='Arial 12 bold')
ent_02=Entry(font='Arial 12 bold')
btn_01=Button(font='Arial 12 bold', text='Узнаем?')

lbl_01.place(x = 10, y = 22)
lbl_02.place(x = 10, y = 52)
ent_01.place(x = 160, y = 22, width=110)
ent_02.place(x = 160, y = 52, width=110)
btn_01.place(x = 300, y = 18, width=80, height=50)

btn_01.bind('<Button-1>', myFunc)


myApp.mainlop()
