from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("455x233")
root.title("slider tutorial")
#myslider=Scale(root,from_=0,to=455)
#myslider.pack()
def getdollar():
    print(f"we have credited {myslider2.get()} dollars to your account")
    tmsg.showinfo("amount credited",f"we have credited {myslider2.get()} dollars to your account")

Label(root,text="how many dollars do you want?").pack()
myslider2=Scale(root,from_=0,to=455,orient=HORIZONTAL,tickinterval=200)
myslider2.set(100)   #we get position of slider at 100 intially default value
myslider2.pack()
Button(root,text="get dollars!",command=getdollar).pack()
root.mainloop()