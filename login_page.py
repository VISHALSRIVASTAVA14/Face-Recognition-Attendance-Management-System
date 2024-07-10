from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
from main import Face_Recognition_System
import os

class login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x810+0+0")
        self.root.title("LOGIN PAGE")
        self.root.resizable(False,False)
        self.root.bind("<Return>",self.enter_function)
        self.root.wm_iconbitmap("52.ico")

        self.email=StringVar()
        self.password=StringVar()

        #background label
        label1=Label(self.root,bg="#720058",relief="solid")
        label1.place(x=3,y=3,width=1353,height=732)

        img1=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\48.jpg")
        img1=img1.resize((900,650),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label2=Label(self.root,image=self.photoimg1)
        label2.place(x=40,y=50,width=900,height=640)

        #login label
        label3=Label(self.root,bg="white")
        label3.place(x=910,y=50,width=400,height=640)

        label4=Label(label3,text="LOGIN",font=("lucida sans",30,"bold"),fg="#720058",bg="white")
        label4.place(x=118,y=30,width=150,height=30)

        #user icon
        img2=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\49.jpg")
        img2=img2.resize((200,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label5=Label(label3,image=self.photoimg2)
        label5.place(x=90,y=60,width=200,height=200)

        #username icon and email entry
        img3=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\50.jpg")
        img3=img3.resize((60,60),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        label6=Label(label3,image=self.photoimg3)
        label6.place(x=45,y=265,width=60,height=60)

        label8=Label(label3,text="ENTER YOUR E-MAIL",font=("lucida sans",13),bg="white")
        label8.place(x=105,y=285)

        entry1=ttk.Entry(label3,font=("lucida sans",12,"bold"),textvariable=self.email)
        entry1.place(x=50,y=320,width=300,height=40)

        #password icon
        img4=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\51.jpg")
        img4=img4.resize((30,40),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        label7=Label(label3,image=self.photoimg4)
        label7.place(x=57,y=382,width=30,height=40)

        label9=Label(label3,text="ENTER YOUR PASSWORD",font=("lucida sans",13),bg="white")
        label9.place(x=100,y=392)

        entry2=ttk.Entry(label3,font=("luicda sans",15),show="*",textvariable=self.password)
        entry2.place(x=50,y=427,width=300,height=40)

        #login button
        b1=Button(label3,text="LOGIN",font=("lucida sans",15,"bold"),bg="#720058",fg="white",relief="groove",cursor="hand2",command=self.login)
        b1.place(x=105,y=520,width=200,height=40)

    #login function
    def enter_function(self,event):
        self.login()
        self.email.set("")
        self.password.set("")

    def login(self):
        if (self.email.get()=="" or self.password.get()==""):
            messagebox.showerror("Error","All entries must be filled to login",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="An@nd3009",database="face_recognition_system")
                my_cursor=conn.cursor()

                my_cursor.execute("SELECT * FROM student WHERE E_MAIL=%s",(self.email.get(),))
                data=my_cursor.fetchall()
                
                if data:
                    for i in data:
                        if (self.password.get()==i[7]):
                            self.new_window=Toplevel(self.root)
                            self.app=Face_Recognition_System(self.new_window)
                            self.email.set("")
                            self.password.set("")
                        else:
                            messagebox.showerror("Error","Invalid password",parent=self.root)
                else:
                    messagebox.showerror("Error","Invalid email",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to : str{es}",parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=login(root)
    root.mainloop()
