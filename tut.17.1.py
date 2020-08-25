from tkinter import  *
root=Tk()
root.title("scroll bar")
root.geometry("455x233")
#for connecting scroll bar to a widget
#1.widget(yscrollcommand=scrollbars.set)
#2.scrollbar.config(command-widget.yview)
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)  #bar comes in y dairection
listbox=Listbox(root,yscrollcommand=scrollbar.set)
for i in range(344):
    listbox.insert(END,f"item {i}")
listbox.pack() 
scrollbar.config(command=listbox.yview)
root.mainloop()