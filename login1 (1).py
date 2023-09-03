from tkinter import *
from PIL import Image,ImageTk
import webbrowser
from tkinter import messagebox
import re
import mysql.connector
def login():
    u_name=un.get()
    pass_word=pw.get()
    data=connection(u_name,pass_word)
    if len(data)>0:
        messagebox.showinfo("success","Welcome to imagecon....your login successfull")
       
    else:
        messagebox.showwarning("warning","Please Enter your Credentials")
        
        
    if check.get()==0:
        messagebox.showwarning("WARNING","please accept our terms and conditions")
        
    
    
w=Tk()
un=StringVar()
pw=StringVar()
w.config(bg="lavender")
w.title("IMAGECON")
w.geometry("1000x500")
pi1=PhotoImage(file='logo.png')
w.iconphoto(False, pi1)
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    
        

def sign():
    w.destroy()
    import signupgui

def google():
    webbrowser.open_new("https://www.google.com/search?gs_ssp=eJzj4tVP1zc0zIgvsUjJrTA0YLRSNagwTkpMSjNMTrK0SLGwNLcwtjKoMDdIMbU0TExMskw1TTK2SPQSyMxNTE9Nzs9TSExOTEnNrQQA_L4WAg&q=imagecon+academy&rlz=1C1CHBD_enIN1016IN1016&oq=imagecon+&aqs=chrome.3.69i59l3j46i175i199i512j69i57j69i60l3.5798j0j7&sourceid=chrome&ie=UTF-8")
def facebook():
    webbrowser.open_new("https://www.facebook.com/imageconIndia/")
def twitter():
    webbrowser.open_new("https://mobile.twitter.com/imageconindia")
    
p1=Image.open("C:/Users/Admin/Pictures/loginpage.png")
l1=p1.resize((600,500),Image.Resampling.LANCZOS)
i1=ImageTk.PhotoImage(l1)
l=Label(w,image=i1,bd=0)
l.pack(side=LEFT)
L1=Label(w,text="WELCOME BACK TO\nIMAGECON",bg="white",fg="violet",font=("Comic Sans MS",20,"bold"))
L1.place(x=250,y=10)

l1=Label(w,text="Login Form",bd=0,font=("Times",15,"bold"))
l1.place(x=700,y=50)
l3=Label(w,text="Username",bg="lavender",fg="purple",font=("Times",13,"bold"))
l3.place(x=700,y=80)
e1=Entry(w,textvariable=un,highlightthickness=2,width=40,font=("Times",10,"bold"))
e1.config(highlightbackground="lightgrey")
e1.place(x=700,y=110)
l4=Label(w,text="Password",bg="lavender",fg="purple",font=("Times",13,"bold"))
l4.place(x=700,y=140)
e2=Entry(w,textvariable=pw,highlightthickness=2,width=40,font=("Times",10,"bold"))
e2.config(highlightbackground="lightgrey")
e2.place(x=700,y=160)
check=IntVar()

condition=Checkbutton(w,text="I agree to Terms & conditions",font=("Arial",9,"bold"),variable=check)
condition.place(x=700,y=190)

b2=Button(w,text="LOGIN",font=("Times",10,"bold"),bg="blue",fg="white",width=35,activebackground="blue",activeforeground="white")
b2.place(x=700,y=220)

l5=Label(w,text="------------OR-----------",font=("Times",9,"bold"),bg="white")
l5.place(x=700,y=250)

l2=Label(w,text="Doesn't have account yet?",font=("Times",10,"bold"),bg="white")
l2.place(x=700,y=280)

b1=Button(w,text="Sign UP",font=("Times",10,"bold"),bg="white",command=sign,fg="darkblue",bd=0)
b1.place(x=850,y=280)

p2=Image.open("C:/Users/Admin/Pictures/chrome.jpg")
l2=p2.resize((60,80),Image.Resampling.LANCZOS)
i2=ImageTk.PhotoImage(l2)

p3=Image.open("C:/Users/Admin/Pictures/facebook.png")
l3=p3.resize((60,80),Image.Resampling.LANCZOS)
i3=ImageTk.PhotoImage(l3)

p4=Image.open("C:/Users/Admin/Pictures/twitter.jpg")
l4=p4.resize((60,80),Image.Resampling.LANCZOS)
i4=ImageTk.PhotoImage(l4)

b3=Button(w,image=i2,bd=0,command=google)
b3.place(x=700,y=360)

b4=Button(w,image=i3,bd=0,command=facebook)
b4.place(x=800,y=360)

b5=Button(w,image=i4,bd=0,command=twitter)
b5.place(x=900,y=360)

def connection(user,passwd):
    host="localhost"
    user="root"
    pw="Vaishu0915"
    db="imagecon"
    con=mysql.connector.connect(host=host,user=user,password=pw,db=db)
    query="select * from login where Username=%s and Password=%s"
    res=(user,passwd)
    cur=con.cursor()
    cur.execute(query,res)
    result=cur.fetchall()
    con.close()
    return result



login
w.mainloop()


