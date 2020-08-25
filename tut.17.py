from tkinter import  *
root=Tk()
root.title("scroll bar")
 #for connecting scroll bar to a widget
#1.widget(yscrollcommand=scrollbars.set)
#2.scrollbar.config(command-widget.yview)
listbox=Listbox(root)
for i in range(344):
    listbox.insert(END,f"item {i}")
listbox.pack()
root.mainloop()