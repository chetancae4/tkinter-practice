#limiting the size of gui display
from tkinter import *
imeganary_tech_root = Tk()
#width x Height
imeganary_tech_root.geometry("644x432")     #this is for opening the screen width=644 and height=432
#width,height
imeganary_tech_root.minsize(200,100)  #even manually you can't reduce screen below 200,100
imeganary_tech_root.maxsize(1000,800)  #even manually you can't maximaize screen above 800,600
shakaib = Label(text="shakaib is a good boy and this is his GUI")
shakaib.pack()
imeganary_tech_root.mainloop()