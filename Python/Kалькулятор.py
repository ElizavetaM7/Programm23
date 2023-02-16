from tkinter import *
from math import *

def myFunc(event):
    lbl_02['text']='Ответ: ' + str(eval(ent_01.get()))

myApp=Tk()
myApp.title("Калькулятор")
myApp.geometry('350x90+600+400')

ent_01=Entry()
btn_01=Button(text='Evaluate...')
lbl_02=Label(font='Arial 12 bold')

ent_01.place(x = 20, y = 20, width=200)
btn_01.place(x = 240, y = 20, width=100)
lbl_02.place(x = 130, y = 55)

btn_01.bind('<Button-1>', myFunc)

myApp.mainloop()
