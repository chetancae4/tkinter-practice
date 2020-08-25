from tkinter import *
i=0
root=Tk()
root.geometry("455x233")
root.title("List box tutorial")
def add():
    global i        #means modification of i is allowed inside the function
    lbx.insert(ACTIVE,f"{i}")  # active means wereever our pointer is there the new value get added above it
    i+=1
lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"First item of list box")  #end means write at the end of line

Button(root,text="add item",command=add).pack()
root.mainloop()