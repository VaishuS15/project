from msilib.schema import Condition
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector

w=Tk()
w.title("IMAGECON")
w.geometry("1000x500")
pi1=PhotoImage(file='logo.png')
w.iconphoto(False, pi1)
w.geometry("1000x500")
p2=Image.open("C:/Users/Admin/Pictures/page.jpg")
l1=p2.resize((1000,500),Image.Resampling.LANCZOS)
i1=ImageTk.PhotoImage(l1)
l=Label(w,image=i1)
l.pack()
L1=Label(w,text="WELCOME TO IMAGECON",bg="white",fg="violet",font=("Comic Sans MS",20,"bold"))
L1.place(x=100,y=100)
L1=Label(w,text="The Next Generation Training",bg="white",fg="black",font=("MS Serif",12,"bold"))
L1.place(x=160,y=140)
l1=Label(w,text="CREATE NEW ACCOUNT",bg="white",font=("Times",20,"bold"))
l1.place(x=600,y=50)
l2=Label(w,text="Email",bg="white",font=("Arial",10,"bold"))
l2.place(x=630,y=100)
e1=Entry(w,bg="Lightblue",width=40,fg="white",font=("Arial",10,"bold"))
e1.place(x=630,y=130)
l3=Label(w,text="Username",bg="white",font=("Arial",10,"bold"))
l3.place(x=630,y=160)
e2=Entry(w,bg="Lightblue",width=40,fg="white",font=("Arial",10,"bold"))
e2.place(x=630,y=190)
l4=Label(w,text="Password",bg="white",font=("Arial",10,"bold"))
l4.place(x=630,y=220)
e3=Entry(w,bg="Lightblue",width=40,fg="white",font=("Arial",10,"bold"))
e3.place(x=630,y=250)
l5=Label(w,text="ConfirmPassword",bg="white",font=("Arial",10,"bold"))
l5.place(x=630,y=280)
e4=Entry(w,bg="Lightblue",width=40,fg="white",font=("Arial",10,"bold"))
e4.place(x=630,y=310)
condition=Checkbutton(w,text="I agree to Terms & conditions",font=("Arial",9,"bold"))
condition.place(x=630,y=340)
b1=Button(w,text="Signup",fg="white",bg="blue",font=("Arial",15,"bold"),width=20,activebackground="red",activeforeground="white",command=w.destroy)
b1.place(x=630,y=400)





w.mainloop()

