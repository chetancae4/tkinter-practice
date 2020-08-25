from tkinter import *
root=Tk()
root.geometry("655x444")
root.title("more concetps on gui")
root.configure(background="red")
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
print(f"{width}x{height}")  #it shows width and height of our gui screen
Button(text="close",command=root.destroy ).pack()  #yes it destroy's window
root.mainloop()