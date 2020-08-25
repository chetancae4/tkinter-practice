from tkinter import *
root=Tk()
root.geometry("733x566")
root.title("pycharm")
def myfunc():
    print("Iam not at all discent")
mymenu=Menu(root)
mymenu.add_command(label="File",command=myfunc)
mymenu.add_command(label="Exit",command=quit)
root.config(menu=mymenu)
root.mainloop()
