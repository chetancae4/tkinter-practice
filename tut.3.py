from tkinter import *
root=Tk()
root.title("my GUI with hach")
#important label options
#text :- adds the text
#bd:-background
#fg:-foreground
#font:- set the font
#padx:- x padding
#pady:- y padding
#relief:-border styling - SUNKEN,RAISED,GROOVE,RIDGE
title_label=Label(text='''Karnataka  Power  Corporation Limited is a Government of Karnataka undertaking registered
 under the companies Act, 1956, and engaged in the development of power projects for the generation of electricity 
 in the State of Karnataka.  The core activities of the Corporation are to identify, construct, establish, operate 
 and maintain power stations and generate ele ctricity.  The scope of activities extends to undertake all initiatives,
  steps and activities that are incidental and ancillary to carryout the core activities.Karnataka  Power 
  Corporation Limited is a Government of Karnataka undertaking registered under the companies Act, 1956, and 
  engaged in the development of power projects for the generation of electricity in the State of Karnataka. '''
,bg="red",fg="white",padx=80,pady=30,font=("comicsansms",10,"bold"),borderwidth=3,relief=SUNKEN)
#important pack opitions
#northeast(ne),northwest(nw),southwest(sw)...........etc  it takes the block towards north west
title_label.pack(anchor="nw")
root.mainloop()

