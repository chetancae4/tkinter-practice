from tkinter import *
root = Tk()                                   #variable classes in tkinter
root.geometry("655x333")                       #Booleanvar,Doublevar,stringvar
def getvals():
    print(f"the value of user name is {uservalue.get()}")
    print(f"the value of password is {passvalue.get()}")
user=Label(root,text="User Name")
password=Label(root,text="Password")
user.grid()
password.grid(row=1)
uservalue=StringVar()
passvalue=StringVar()
userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
Button(text="submit",command=getvals ).grid(column=1)
root.mainloop()