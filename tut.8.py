from tkinter import *
root = Tk()
def getvals():
    print("submitting form")
    print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}")
    with open("record.txt","a") as f:   #oepning file in append mode
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}\n ")
root.geometry("655x333")

Label(root,text="welcome to hac travels",font="comicsansms 13 bold",pady=20).grid(row=0,column=3)
name=Label(root,text="name")
phone=Label(root,text="phone")
gender=Label(root,text="gender")
emergency=Label(root,text="emergency contact")
paymentmode=Label(root,text="payment mode")
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=StringVar()

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue)


nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)
#check box
foodservice=Checkbutton(text="want to pre book your meals?",variable=foodservicevalue)
foodservice.grid(row=6,column=3)
#button and packing it and assaigning it a command
Button(text="submit to harry travels",command=getvals).grid(row=7,column=3)


root.mainloop()