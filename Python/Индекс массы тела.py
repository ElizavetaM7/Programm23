from tkinter import *
import tkinter.messagebox

def myFunc(event):
    h=float(ent_01.get())/100
    w=float(ent_02.get())
    ИМТ=w/(h*h)
    if ИМТ<18.5:
        s='Недостаточный вес!!!'
    elif ИМТ<24.9:
        s='Вес в норме:)'
    else:
        s='Избыточный вес!!!'
    imt=tkinter.messagebox.showinfo(message=s)

myApp=Tk()
myApp.title("Подсчет ИМТ")
myApp.geometry('320x100+600+400')

lbl_01=Label(text='Рост(см): ',font='Arial 12 bold')
lbl_02=Label(text='Вес(кг): ',font='Arial 12 bold')
ent_01=Entry(font='Arial 12 bold')
ent_02=Entry(font='Arial 12 bold')
btn_01=Button(font='Arial 12 bold', text='ИМТ')

lbl_01.place(x = 20, y = 22)
lbl_02.place(x = 20, y = 52)
ent_01.place(x = 130, y = 22, width=40)
ent_02.place(x = 130, y = 52, width=40)
btn_01.place(x = 220, y = 18, width=60, height=50)

btn_01.bind('<Button-1>', myFunc)

myApp.mainloop()
