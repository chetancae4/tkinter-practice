### i not got aptitude
import os
import wolframalpha
import wikipedia
from tkinter import *
import tkinter.messagebox
import speech_recognition as sr
import time
while True:
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("speak something.......")
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            if text=="stop":
                break
            else:
                window=Tk()
                window.geometry("700x600")
                try:
                    app_id="HGJ7YK-2RXQ7UVKHW"
                    client=wolframalpha.Client(app_id)
                    asnwer=next(res.results).text

                    label1=Label(window,justfiy=LEFT,compound=CENTER,padx=10,text=asnwer,font="tiems 15 bold")
                    label1.pack()
                    window.after(5000,lambda: window.destroy())  #5000 micro second
                    mainloop()
                except:
                    asnwer=wikipedia.summary()
                    label1 = Label(window, justfiy=LEFT, compound=CENTER, padx=10, text=asnwer, font="tiems 15 bold")
                    label1.pack()
                    window.after(5000,lambda: window.destroy())  # 5000 micro second
                    mainloop()
        except:
            answer="sorry we can't here you"
            print(answer)












































