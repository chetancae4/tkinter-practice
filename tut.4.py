from tkinter import *
root = Tk()
root.geometry("655x333")
f1=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,pady=42,fill="y")
f2=Frame(root,bg="grey",borderwidth=8,relief=SUNKEN)
f2.pack(side=TOP,fill="x")
l=Label(f1,text="project Tkinter-pycharm")
l.pack(pady=142)
l=Label(f2,text="welcome to sublime text",font="Helvetica 16 bold",fg="red")
l.pack(pady=142)

root.mainloop()