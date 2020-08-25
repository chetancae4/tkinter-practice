from tkinter import *
root = Tk()
root.geometry("655x333")
frame=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")
def hello():
    print("yes i recognized you")
def name():
    print('my name is hach')
b1=Button(frame,fg="red", text="check",command=hello,padx=20) #pax means width of each button
b1.pack(side=LEFT)
b2=Button(frame,fg="red", text="name",command=name,padx=20)
b2.pack(side=LEFT )
b3=Button(frame,fg="red", text="print now",padx=20)
b3.pack(side=LEFT)
b4=Button(frame,fg="red", text="print now",padx=20)
b4.pack(side=LEFT)



root.mainloop()