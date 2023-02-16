from tkinter import *
from tkinter import messagebox
from random import *
from tkinter.colorchooser import askcolor

wnd=Tk()
wnd.title('Графический редактор')
wnd.geometry('1920x1080')
brush_size=4
brush_color='black'

def paint(event):
    global brush_size
    global brush_color
    x1=event.x-brush_size
    x2=event.x+brush_size
    y1=event.y-brush_size
    y2=event.y+brush_size
    canvas.create_oval(x1,y1,x2,y2, fill=brush_color, outline=brush_color)

def brush_size_change(new_size):
    global brush_size
    brush_size=new_size

def brush_color_change(new_color):
    global brush_color
    brush_color=new_color

def choose_color(self):
    self.eraser_on = False
    self.color=askcolor(color=self.color)[1]

frame_01=Frame(width=500)
frame_02=Frame()
canvas=Canvas(frame_02,width=1000, height=1000, bg='white')
btn_01=Button(frame_01, text='Круг', command=lambda:
              canvas.create_oval(120,20,400,100,fill=brush_color, width=brush+size))
btn_02=Button(frame_01, text='Линия',command=lambda:
              canvas.create_line(0,120,100,200,200,100,300,300,400,400, width=brush_size, fill=brush_color))
btn_03=Button(frame_01, text='Квадрат',command=lambda:
              canvas.create_rectangle(20,20,100,100, width=brush_size, fill=brush_color))
btn_04=Button(frame_01, text='Толстая линия', command=lambda:
              brush_size_change(10))
btn_05=Button(frame_01, text='Тонкая линия', command=lambda:
              brush_size_change(2))
btn_06=Button(frame_01, text='Средняя линия', command=lambda:
              brush_size_change(6))
btn_07=Button(frame_01, text='Черный', command=lambda:
              brush_color_change('black'))
btn_08=Button(frame_01,text='Розовый', fg='pink', command=lambda:
              brush_color_change('pink'))
btn_09=Button(frame_01,text='Оливковый', fg='olive', command=lambda:
              brush_color_change('olive'))
btn_10=Button(frame_01,text='Синий', fg='blue', command=lambda:
              brush_color_change('blue'))
btn_11=Button(frame_01, text='Ластик', command=lambda:
              brush_color_change('white'))
btn_12=Button(frame_01, text='Очистить', command=lambda:
              canvas.delete('all'))

canvas.bind('<B1-Motion>', paint)

frame_01.pack(side='left')
frame_02.pack(expand=True, fill='both')
canvas.pack(expand=True, fill='both')
btn_01.pack()
btn_02.pack()
btn_03.pack()
btn_04.pack()
btn_05.pack()
btn_06.pack()
btn_07.pack()
btn_08.pack()
btn_09.pack()
btn_10.pack()
btn_11.pack()
btn_12.pack()

wnd.mainloop()
