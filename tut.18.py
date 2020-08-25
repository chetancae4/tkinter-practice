#create a gui window which takes as input width and height
#and upon clicking apply it should be able to change its size accordingly
from tkinter import *
def update():
    print("updating the gui")
    root.geometry(f"{width.get()}x{height.get()}")

root=Tk()
width=StringVar()
height=StringVar()
Entry(root,textvariable=width).pack()
Entry(root,textvariable=height).pack()
Button(root,text="apply",command=update).pack()
root.mainloop()
