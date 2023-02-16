from tkinter import *
import tkinter.messagebox

wnd = Tk() #имя можно и на русском, и на английском
wnd.title("Моя программа")
wnd.geometry('600x400+300+150')  #'размер'+отступ слева+отступ сверху

lbl=Label(wnd,
          text="Приветствую",
          font="Times 20 bold italic",
          fg="red")

lbl.place(x = 70, y = 50)

ent = Entry(width = 30, font="Times 20 bold italic")
ent.place(x=30, y=100)

a=tkinter.messagebox.showinfo(message="ВНИМАНИЕ!")

btn=Button(text="Кнопка")
btn.place(x=470, y=105)

wnd.mainloop()
