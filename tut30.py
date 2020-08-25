import pygame
from tkinter import *
import os
root=Tk()
root.geometry("400x300")
pygame.mixer.init()
n=0
def start_stop():
    global n
    n=n+1
    if n==1:
        song_name=songs_listbox.get()
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(0)    #if you want to play in loop we have to make -1
    elif(n%2)==0:
        pygame.mixer.music.pause()
    elif(n%2)!=0:
        pygame.mixer.music.unpause()

l1=Label(root,text="Music player",font="times 20")
l1.grid(row=1,column=1)

b2=Button(root,text='play',command=start_stop)
b2.grid(row=4,column=1,padx=100)
songs_list=os.listdir()
songs_listbox=StringVar(root)
songs_listbox.set("select song")
menu=OptionMenu(root,songs_listbox,*songs_list)
menu.grid(row=4,column=4)
root.mainloop()
