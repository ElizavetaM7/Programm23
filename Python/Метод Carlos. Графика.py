from tkinter import *
from tkinter.colorchooser import askcolor

myApp=Tk()
myApp.title("Графика")
myApp.geometry('800x550+250+100')

frame_01=Frame(width=200, relief='sunken')
frame_02=Frame(myApp)
canvas=Canvas(frame_02, width=1000, height=1000, bg='pale turquoise')

buttons=[]
for i in range(10):
    buttons.append(Button(frame_01,text='Кнопка'+str(i+1)))


for b in buttons:
    b.pack()


canvas.create_rectangle(20,20,100,100, fill = 'cyan')
canvas.create_oval(120,20,400,100)
canvas.create_line(0,200,100,130,300,400,400,300,width=30, fill='light blue')

frame_01.pack(side='left')
frame_02.pack()
canvas.pack(expand=True, fill = 'both')

myApp.mainloop()
