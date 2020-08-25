from tkinter import *
from PIL import ImageTk,Image
root=Tk()
def every_100(text):
    final_text=""
    for i in range(0,len(text)):
        final_text+=text[i]
        if i%100==0 and i!=0 :    #here for every 100th line we are moving to next line 0%100=0 so we are avoiding it
            final_text+='\n'
    return final_text
root.title("hac news-apka apna akbar")
root.geometry("1000x1000")
texts=[]
photos=[]
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text=f.read()
        texts.append(every_100(text))
    image=Image.open(f"{i+1}.jpg")
    #resize this image
    #TODO:resize this images
    image=image.resize((250,200),Image.ANTIALIAS)   #antialias is for getting clear photo
    photos.append(ImageTk.PhotoImage(image))
f0=Frame(root,width=800,height=70)
Label(f0,text="code with hac news",font="lucida 25 bold").pack()
Label(f0,text="jun29 2020",font="lucida 13 bold").pack()
f0. pack()
f1=Frame(width=900,height=200)
Label(f1,text=texts[0],padx=22,pady=22).pack(side="left")
Label(f1,image=photos[0],anchor="e").pack()
f1.pack(anchor="w")
f2=Frame(width=900,height=200)
Label(f2,text=texts[1],padx=40,pady=22).pack(side="left")
Label(f2,image=photos[1],anchor="e").pack()
f2.pack(anchor="w")
f3=Frame(width=900,height=200)
Label(f3,text=texts[2],padx=26 ,pady=22).pack(side="left")
Label(f3,image=photos[2],anchor="e").pack()
f3.pack(anchor="w")

root.mainloop()