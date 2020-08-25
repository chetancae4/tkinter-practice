from tkinter import *
root=Tk()
root.geometry("455x233")
root.title("status bar tutorial")
def upload():
    import time
    statusvar.set("Busy......")
    sbar.update()
    time.sleep(2)
    statusvar.set("Ready Now")
statusvar=StringVar()
statusvar.set("Ready")
sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="upload",command=upload).pack()
root.mainloop()