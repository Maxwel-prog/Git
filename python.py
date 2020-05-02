#git
from tkinter import *

root = Tk()
root.geometry("650x370+350+150")
# Не получилось найти ico картинку для логотипа, поставь пожалуйста
root.title("Test")
root.resizable(False, False)
root.config(bg = "light green")

btn = Button(root, text ="Button", bg ="#196", bd = 8)
btn.pack()

btn2 = Button(root, text ="Button2", bg = "#195",bd = 6)
btn2.pack()

root.mainloop()





