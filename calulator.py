from tkinter import *
def click(event):
    global scvalue
    text=event.widget.cget("text")    #this is to get the number that we press
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())  #eval is a inbuilt function that evaluate addition,sub,mul....etc
        scvalue.set(value)
        screen.update()

    elif text=="c":
        scvalue.set("")
        screen.update()
    else:

        scvalue.set(scvalue.get()+text)
        screen.update()
root=Tk()
root.geometry("644x1000")
root.title("hac's calculator")
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,padx=10,pady=10)    #intarnal padding
f=Frame(background="grey")
f.pack()
b=Button(f,text="9",font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)
b=Button(f,text="8",font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)
b=Button(f,text="7",font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)
f=Frame(background="grey")
f.pack()
b=Button(f,text="6",font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)
b=Button(f,text="5",font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)
b=Button(f,text="4",font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)
f=Frame(background="grey")
f.pack()
b=Button(f,text="3",font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)
b=Button(f,text="2",font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)
b=Button(f,text="1",font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)
f=Frame(background="grey")
f.pack()
b=Button(f,text="0",font="lucida 35 bold",padx=7,pady=5)
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)
b=Button(f,text="-",font="lucida 40 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)
b=Button(f,text="*",font="lucida 35 bold",padx=9,pady=5)
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)
f=Frame(background="grey")
f.pack()
b=Button(f,text="/",font="lucida 35 bold",padx=9,pady=5)
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)
b=Button(f,text="%",font="lucida 30 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)
b=Button(f,text="=",font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)
f=Frame(background="grey")
f.pack()
b=Button(f,text="c",font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)
b=Button(f,text="5",font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)
b=Button(f,text="4",font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)

root.mainloop()