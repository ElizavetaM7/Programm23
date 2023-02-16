from tkinter import *
from tkinter.colorchooser import askcolor

def move(event):
    myApp.title(str(event.x)+'  '+str(event.y))

def press(event):
    global x1, y1
    x1=event.x
    y1=event.y

def release(event):
    global x1, y1, r
    x2=event.x
    y2=event.y
    if r.get()==1:
        canvas.create_rectangle(x1,y1, x2, y2, width=w.get(), fill=color_button['bg'], outline=color_button['bg'])
    elif r.get()==2:
        canvas.create_oval(x1, y1, x2, y2,width=w.get(), fill=color_button['bg'],outline=color_button['bg'])

def ColorChose_1():
    color_button['bg']=askcolor(title="Выбор цвета заливки")[1]

def ColorChose_2():
    color_line_button['bg']=askcolor(title="Выбор цвета контура")[1]
    
def wheel(event):
    w.set(w.get()+event.delta/abs(event.delta))
    if w.get<0:
        w.set(0)
    elif w>99:
        w.set(99)

myApp=Tk()
myApp.title("Графика")
myApp.geometry('800x550+250+100')
myApp.minsize(width=400, height=200)

frame_01=Frame(width=200, bd=1, relief=RAISED)
frame_02=Frame(bd=1, relief=SUNKEN)
canvas=Canvas(frame_02, bg="white", width=1000, height=1000)
frame_r1=LabelFrame(frame_01, text="Инструменты", width=180, height=180)
r=IntVar()
rb_01=Radiobutton(frame_r1, text="Прямоугольник", variable=r, value=1)
rb_02=Radiobutton(frame_r1, text="Элипс", variable=r, value=2)
color_button=Button(frame_01, text="Цвет заливки", width=20, command=ColorChose_1)
color_line_button=Button(frame_01, text="Цвет контура ", width=20, command=ColorChose_2)
w=IntVar()  # ширина контура переменная
w.set(10)
spin=Spinbox(frame_01, from_=0, to=99, width=3, textvariable=w)

frame_01.pack(side="left", fill="y")
frame_02.pack(fill="both", expand=True)
canvas.pack(fill="both", expand=True)
frame_r1.place(x=10, y=10)
rb_01.place(x=10, y=10)
rb_02.place(x=10, y=30)
color_button.place(x=23, y=200)
color_line_button.place(x=23, y=230)
spin.place(x=60, y=260)

canvas.bind('<Motion>', move)
canvas.bind('<ButtonPress-1>', press)
canvas.bind('<ButtonRelease-1>', release)
canvas.bind('<MouseWheel>', wheel)

myApp.mainloop()
