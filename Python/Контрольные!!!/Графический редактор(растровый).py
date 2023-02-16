#главное меню:
#Справка, в ней тот, кто написал программу
#Файл

#Панель инструментов - слева



from tkinter import *
from tkinter.messagebox import *
from tkinter.colorchooser import askcolor

# класс Paint
class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

# выход из программы  
def close_win():
  if askyesno("Выход", "Вы уверены?"):
    root.destroy()

# вывод справки    
def about():
  showinfo("Разработчик программы", "Мамзелева Елизавета, УГИ-216004")

def main():
    global root
    root = Tk()
    root.geometry("800x600+300+300")
    app = Paint(root)
    m = Menu(root)
    root.config(menu=m)

    fm = Menu(m)
    m.add_cascade(label="Файл", menu=fm)
    fm.add_command(label="Выход", command=close_win)

    hm = Menu(m)
    m.add_cascade(label="Справка", menu=hm)
    hm.add_command(label="О программе", command=about)
    root.mainloop()

if __name__ == "__main__":
    main()

##myApp=Tk()
##myApp.title("Графика")
##myApp.geometry('800x550+250+100')
##myApp.minsize(width=400, height=200)

##frame_01=Frame(myApp, width=200, bd=1, relief=RAISED)
##frame_02=Frame(bd=1, relief=SUNKEN)
##canva=Canvas(frame_02, bg="white", width=1000, height=1000)
##frame_r1=LabelFrame(frame_01, text="Инструменты", width=180, height=180)
##
##
##
##frame_01.pack(side="left", fill="y")
##frame_02.pack(fill="both", expand=True)
##canva.pack(fill="both", expand=True)
##frame_r1.place(x=10, y=10)



##
##
### выход из программы  
##def close_win():
##  if askyesno("Выход", "Вы уверены?"):
##    root.destroy()
##
### вывод справки    
##def about():
##  showinfo("Разработчик программы", "Мамзелева Елизавета, УГИ-216004")
  
# функция для создания главного окна
##def main():
##    global root
##    root = Tk()
##    root.geometry("800x600+300+300")
##    app = Paint(root)
##    m = Menu(root)
##    root.config(menu=m)
##
##    fm = Menu(m)
##    m.add_cascade(label="Файл", menu=fm)
##    fm.add_command(label="Выход", command=close_win)
##
##    hm = Menu(m)
##    m.add_cascade(label="Справка", menu=hm)
##    hm.add_command(label="О программе", command=about)
##    root.mainloop()
##
##if __name__ == "__main__":
##    main()

myApp.mainloop()
