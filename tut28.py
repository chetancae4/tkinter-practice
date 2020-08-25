import requests
from tkinter import *
import sys
import random
def color_change():
    list=["red","green","white","blue","black"]
    virus.config(background=random.choice(list))
    virus.after(200,color_change)  #200 micro second
root=Tk()
root.geometry("700x500")
virus=Label(root,text="you have a virus warning",font="times 50 bold")
virus.grid(row=2,column=0,padx=20,pady=20)
color_change()       #it is a function we are calling
root.mainloop()