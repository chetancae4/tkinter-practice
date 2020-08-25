from tkinter import *
root = Tk()
def harry(event):
    print(f"you clicked on the button at {event.x},{event.y}")
root.title("events in tkinter")
root.geometry("644x344")
widget=Button(root,text="click me please")
widget.pack()
widget.bind('<Button-1>',harry)
widget.bind('<Double-1>',quit)   #if you double clicked it will be close


root.mainloop()













