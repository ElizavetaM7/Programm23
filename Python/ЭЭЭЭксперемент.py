from tkinter import *
from math import *
import tkinter.messagebox


def myFunc(event):
    lbl_01['text']=''
    lbl_02['text']='Хочешь узнать кое-что интересное?'
    btn_01['text']='Конечно!'
def myFunc2(event):
    lbl_02['text']=''
    lbl_03['text']='Давай познакомимся!?'
    

myApp=Tk()
myApp.title=""
myApp.geometry('400x400+500+200')

lbl_01=Label(text='Доброго времени суток!', font='Arial 16 bold')
lbl_02=Label(font='Arial 14 bold')
lbl_03=Label(font='Arial 16 bold')

btn_01=Button(text='Привет', font='Arial 16 bold')

lbl_01.place(x=75, y=50)
lbl_02.place(x=35, y=50)
lbl_03.place(x=75, y=50)

btn_01.place(x=155, y=100)

btn_01.bind('<Button-1>', myFunc)
btn_01.bind('<Button-1>', myFunc2)

#DON'T WORK!!!
myApp.mainloop()
