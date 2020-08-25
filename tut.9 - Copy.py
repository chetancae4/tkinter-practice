from tkinter import *
root = Tk()
canvas_width=800
canvas_height=400
root.title("code with hac")
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget=Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()
#the line goes from (x1,y1) to (x2,y2)
can_widget.create_line(0,0,800,800,fill='red')      #(x1,y1,x2,y2)
can_widget.create_line(0,800,800,0,fill='green')
#creating rectangle coardinates=top left and bottom right
can_widget.create_rectangle(10,10,700,300,fill='red')
can_widget.create_text(200,200,text="hac me")
#creating oval it will come in rectangle so we need to give rectangular coardinate
can_widget.create_oval(344,233,244,355)
root.mainloop()