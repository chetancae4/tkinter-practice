from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newfile():
    global file
    root.title("untitled - Notepad")
    file=None
    Textarea.delete(1.0,END)   #1st row and 0 th column
def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"- Notepad")
        Textarea.delete(1.0,END)
        f=open(file,"r")
        Textarea.insert(1.0,f.read())
        f.close()
def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file==None:
            file=None
        else:
            #save as new file
            f=open(file,"w")
            f.write(Textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
            print("File saved")
    else:
        f = open(file, "w")
        f.write(Textarea.get(1.0, END))
        f.close()
def quitapp():
    root.destroy()
def cut():
    Textarea.event_generate(("<<Cut>>"))  #it autometically genarate cut operation
def copy():
    Textarea.event_generate(("<<Copy>>"))
def paste():
    Textarea.event_generate(("<<Paste>>"))
def about():
    showinfo("Note pad","notepad by hach")
if __name__=='__main__':
    #basic tkinter setup
    root=Tk()
    root.title("untititled Notepad")
    root.geometry("644x788")

    #Add text area
    Textarea=Text(root,font="lucida 13")
    file=None
    Textarea.pack(expand=True,fill=BOTH)

    #lets create a menu bar
    menubar=Menu(root)
    #File menu starts
    FileMenu=Menu(menubar,tearoff=0)  #it removes dotted line in submenu list if you are not removing its fine
    #to open newfile
    FileMenu.add_command(label="new",command=newfile)
    #to open already existing file
    FileMenu.add_command(label="open",command=openfile)
    #to save the current file
    FileMenu.add_command(label="save",command=savefile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitapp)
    menubar.add_cascade(label="File",menu=FileMenu)
    #FileMenu ends

    #Edit menu starts
    EditMenu=Menu(menubar,tearoff=0)
    #to give the feature of cut,copy and paste
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    menubar.add_cascade(label="Edit",menu=EditMenu)
    #edit menu ends
    #help menu starts
    HelpMenu=Menu(menubar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    menubar.add_cascade(label="Help",menu=HelpMenu)


    root.config(menu=menubar)
    #adding scrollbar
    scroll=Scrollbar(Textarea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=Textarea.yview)
    Textarea.config(yscrollcommand=scroll.set)


    root.mainloop()