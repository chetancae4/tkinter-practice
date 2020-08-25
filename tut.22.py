from tkinter import *
def newfile():
    pass
def openfile():
    pass
def savefile():
    pass
def quitapp():
    pass
def cut():
    pass
def copy():
    pass
def paste():
    pass
def about():
    pass
if __name__=='__main__':
    #basic tkinter setup
    root=Tk()
    root.title("untititled Notepad")
    root.geometry("644x788")

    #Add text area
    Textarea=Text(root,font="lucida 13")
    file=None

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
    EditMenu.add_cascade(label="Edit",menu=EditMenu)
    menubar.add_cascade(label="Edit",menu=EditMenu)
    #edit menu ends
    #help menu starts
    HelpMenu=Menu(menubar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    menubar.add_cascade(label="Help",menu=HelpMenu)






    root.config(menu=menubar)

root.mainloop()