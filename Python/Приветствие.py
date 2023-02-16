from tkinter import *

def myFunc(event):
    lbl_02['text']='Привет, '+ent_01.get()

myApp=Tk()
myApp.geometry('350x150+300+150')

lbl_01=Label(text='Представьтесь')
ent_01=Entry()
btn_01=Button(text='Ok')
lbl_02=Label()

lbl_01.place(x = 15, y = 18)
ent_01.place(x = 120, y = 18)
btn_01.place(x = 260, y = 15, width=55)
lbl_02.place(x = 130, y = 65)

btn_01.bind('<Button-1>', myFunc)

myApp.mainloop()
