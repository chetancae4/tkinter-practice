from tkinter import *
t=0
#even though there is error still we are getting output
root=Tk()
def set_timer():
    global t
    t=t+int(x.get())
    print(t)
    return t
def countdown():
    global t
    if t>0:
        p.config(text=t)
        t=t-1
        p.after(1000,countdown)
    elif t==0:
        print("en")
        p.config(text="goo")


root.geometry("700x800")
p=Label(root,font='times 20')
p.grid(row=1,column=2)
y=Label(root,text="enter the  count")
y.grid(row=2,column=1)
times=StringVar()
x=Entry(root,textvariable=times)
x.grid(row=2,column=2)
b1=Button(root,text="set",width=20,command=set_timer)
b1.grid(row=3,column=2)
b2=Button(root,text="start",width=20,command=countdown)
b2.grid(row=4,column=2)






root.mainloop()