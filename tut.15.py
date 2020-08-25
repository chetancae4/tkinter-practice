from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("455x233")
root.title("Radio button tutorial")
def order():
    tmsg.showinfo("order recieved", f"we have recieved your oreder for {var.get()}.thanks for ordering")

var=StringVar()   #creating a variable of intiger var takes value
var.set('xyz')   #you can give anything other than values of radio xyz,abc,......if we not write this it will select all orders by default try it by removing it ypu will understand
Label(root,text="what would you like to have sir?",font="lucida 19 bold",justify=LEFT,padx=14).pack()
radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value="dosa").pack(anchor="w") #use anchor if you want burron at left
radio=Radiobutton(root,text="Idly",padx=14,variable=var,value="idly").pack(anchor="w")
radio=Radiobutton(root,text="Paratha",padx=14,variable=var,value="paratha").pack(anchor="w")
radio=Radiobutton(root,text="Pav Bhaji",padx=14,variable=var,value="pav bhaji").pack(anchor="w")
Button(root,text="Order",command=order).pack()
root.mainloop()