from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("733x566")
root.title("pycharm")
def myfunc():
    print("Iam not at all discent")
def help():
    print("i will help you hac")
    tmsg.showinfo("Help","hac will help you")
def rate():
    print("rate us")
    value=tmsg.askquestion("experiance","was your experiance is good?")
    print(value)
    if value=="yes":
        msg="Great rate us please in app store"
    else:
        msg="tell us what went wrong we will call you soon"
    tmsg.showinfo("Message",msg)
def hacs():
    ans=tmsg.askretrycancel("hac se dosti karlu?","sorry hac se nahi banegi dosti")
    msg="sorry vho intrested nahi hai"
    if ans:
        tmsg.showinfo("Message", msg)
    else:
        tmsg.showinfo("Message", "it's a good decision")
filemenu=Menu(root)
m1=Menu(filemenu)
m1.add_command(label="New project",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_separator()
m1.add_command(label="Save As",command=myfunc)
m1.add_command(label="Print",command=myfunc)
root.config(menu=filemenu)
filemenu.add_cascade(label="File",menu=m1)
m2=Menu(filemenu)
m2.add_command(label="cut",command=myfunc)
m2.add_command(label="copy",command=myfunc)
m2.add_separator()
m2.add_command(label="paste",command=myfunc)
m2.add_command(label="find",command=myfunc)
root.config(menu=filemenu)
filemenu.add_cascade(label="Edit",menu=m2)

m3=Menu(filemenu)
m3.add_command(label="Help",command=help)
m3.add_command(label="rate us",command=rate)
m3.add_command(label="hacs",command=hacs)
filemenu.add_cascade(label="Help",menu=m3)
root.config(menu=filemenu)
root.mainloop()
