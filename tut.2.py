from tkinter import *
from PIL import Image,ImageTk   #this is for jpg format
imeganary_tech_root = Tk()
imeganary_tech_root.geometry("1500x1500")
#photo=PhotoImage(file="1.JPG").
image=Image.open("1.JPG")
photo=ImageTk.PhotoImage(image)
varun_label=Label(image=photo)
varun_label.pack()
imeganary_tech_root.mainloop()

