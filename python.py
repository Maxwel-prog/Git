#git
from tkinter import *
from tkinter import messagebox
import time

# само окно
root = Tk()
root.geometry("650x370+350+150")
# Не получилось найти ico картинку для логотипа, поставь пожалуйста
root.title("Test")
root.resizable(False, False)
root.config(bg = "light green")

#Меню
mb =  Menubutton ( root, text = "Menu", relief = RAISED,bg ="#196", bd = 8 )
mb.grid()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu
bt1Var  = IntVar()
bt2Var = IntVar()

mb.menu.add_checkbutton ( label = "Butten1 ",
                          variable = bt1Var )
mb.menu.add_checkbutton ( label = "Butten2",
                          variable = bt2Var )
mb.pack()


def helloCallBack():
    msg = messagebox.showinfo("Ok","Ok",)


#Первая кнопка
btn = Button(root, text ="Button", bg ="#196", bd = 8,command = helloCallBack)
btn.place(x =2, y=0)
btn.pack()

# notepad(Влад, сделай здесь блокнот пожалуйста)
btn2 = Button(root, text ="notepad", bg = "#195",bd = 8)
btn2.place(x =0, y=0)
btn.pack()


def check_time():
    btn_time["text"] =time.strftime("%H:%M:%S")

#Time
btn_time = Button(root,text ="time",command = check_time, bg = "green", bd = 8)
btn_time.pack()


root.mainloop()





