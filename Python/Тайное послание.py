from tkinter import *

def press1(event):
    lbl_01['text']='Ты ещё не готов'
    lbl_01['bg']='white'
def press2(event):
    lbl_01['bg']='black'
    lbl_01['fg']='black'
def press3(event):
    lbl_01['fg']='red'
    lbl_01['text']='Ха-ха'
    lbl_01['bg']='black'

wnd=Tk()
wnd.title("Моё окно")
wnd.geometry('800x500+300+100')

lbl_01 = Label(font="Times 20 bold italic",
               text="Тайное послание",
               bg='yellow',
               fg='magenta')
lbl_01.place(x=300, y=20)


btn=Button(font="Times 15 bold italic",
               text="Открыть",
               bg='SteelBlue',
               fg='navy')
btn.place(x=350, y=200)
btn.bind('<Button-1>', press1)
btn.bind('<Button-2>', press2)
btn.bind('<Button-3>', press3)
#ent = Entry(width = 30,
#            bg='light gray',
#            font="Times 20 bold italic")
#ent.place(x=30, y=100)

wnd.mainloop()
