from tkinter import*
from tkinter import messagebox
from tkinter import ttk #stylish toolkit
from PIL import Image,ImageTk
from student_details import student
from train_data import train
from face_recognition import face_recognition
from attendance_interface import attendance
from developer import developer
from chatbot import chatbot
import os


class Face_Recognition_System:
    def __init__(self,root): #constructor
        self.root=root
        self.root.geometry("1360x810+0+0")
        self.root.title("Face Recognition System")
        self.root.resizable(width=False,height=False)
        self.root.wm_iconbitmap("52.ico")

        #first image
        img=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\4.jpg") #r is used for converting the forward slash in backslash
        img=img.resize((450,130),Image.ANTIALIAS)# ANTIALIAS converts high level image to low level image
        self.photoimg=ImageTk.PhotoImage(img)
        
        label1=Label(self.root,image=self.photoimg,relief="solid")
        label1.place(x=1,y=2,width=450,height=130)

        #second image
        img2=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\2.jpg")
        img2=img2.resize((460,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label2=Label(self.root,image=self.photoimg2,relief="solid")
        label2.place(x=450,y=2,width=450,height=130)

        #third image
        img3=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\3.jpg")
        img3=img3.resize((458,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        label3=Label(self.root,image=self.photoimg3,relief="solid")
        label3.place(x=898,y=2,width=458,height=130)

        #background image
        img4=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\5.png")
        img4=img4.resize((1360,555),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        label4=Label(self.root,image=self.photoimg4,relief="solid")
        label4.place(x=1,y=180,width=1356,height=555)

        #heading
        label5=Label(self.root,text="FACE RECOGNITION ATTENDENCE MANAGEMENT SYSTEM",font=("lucida sans",15,"bold"),width=50,height=2,bg="purple",fg="white",relief="solid")
        label5.place(x=1,y=129,width=1356)

        #student detail button
        img5=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\6.jpg")
        img5=img5.resize((200,100),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(label4,image=self.photoimg5,cursor="hand2",command=self.std_details,relief="solid")
        b1.place(x=225,y=90,width=200,height=100)
        
        b1=Button(label4,text="STUDENT DETAILS",font=("lucida sans",10,"bold"),bg="purple",fg="white",cursor="hand2",command=self.std_details,relief="solid")
        b1.place(x=225,y=180,width=200,height=30)

        #face recognition button
        img6=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\1.jpg")
        img6=img6.resize((200,100),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b2=Button(label4,image=self.photoimg6,cursor="hand2",command=self.face_recognition_btn,relief="solid")
        b2.place(x=470,y=90,width=200,height=100)

        b2=Button(label4,text="FACE RECOGNITION",font=("lucida sans",10,"bold"),bg="purple",fg="white",cursor="hand2",command=self.face_recognition_btn,relief="solid")
        b2.place(x=470,y=180,width=200,height=30)

        #attendence button
        img7=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\7.jpg")
        img7=img7.resize((200,100),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b3=Button(label4,image=self.photoimg7,cursor="hand2",relief="solid",command=self.attendance)
        b3.place(x=715,y=90,width=200,height=100)

        b3=Button(label4,text="ATTENDANCE",font=("lucida sans",10,"bold"),bg="purple",fg="white",cursor="hand2",relief="solid",command=self.attendance)
        b3.place(x=715,y=180,width=200,height=30)

        #chatbot button
        img8=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\8.jpg")
        img8=img8.resize((200,100),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b4=Button(label4,image=self.photoimg8,cursor="hand2",relief="solid",command=self.chatbot_btn)
        b4.place(x=960,y=90,width=200,height=100)

        b4=Button(label4,text="CHATBOT",font=("lucida sans",10,"bold"),bg="purple",fg="white",cursor="hand2",relief="solid",command=self.chatbot_btn)
        b4.place(x=960,y=180,width=200,height=30)

        #train data button
        img9=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\9.jpg")
        img9=img9.resize((200,100),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b5=Button(label4,image=self.photoimg9,cursor="hand2",command=self.train_data,relief="solid")
        b5.place(x=225,y=280,width=200,height=100)

        b5=Button(label4,text="TRAIN DATA",font=("lucida sans",10,"bold"),bg="purple",fg="white",cursor="hand2",relief="solid")
        b5.place(x=225,y=370,width=200,height=30)

        #gallery button
        img10=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\10.jpg")
        img10=img10.resize((200,100),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b6=Button(label4,image=self.photoimg10,cursor="hand2",command=self.gallery,relief="solid")
        b6.place(x=470,y=280,width=200,height=100)

        b6=Button(label4,text="GALLERY",cursor="hand2",font=("lucida sans",10,"bold"),bg="purple",fg="white",command=self.gallery,relief="solid")
        b6.place(x=470,y=370,width=200,height=30)

        #developer button
        img11=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\11.jfif")
        img11=img11.resize((200,100),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b7=Button(label4,image=self.photoimg11,cursor="hand2",relief="solid",command=self.developer)
        b7.place(x=715,y=280,width=200,height=100)

        b7=Button(label4,text="DEVELOPER",cursor="hand2",font=("lucida sans",10,"bold"),bg="purple",fg="white",relief="solid",command=self.developer)
        b7.place(x=715,y=370,width=200,height=30)

        #exit button
        img12=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\12.jpg")
        img12=img12.resize((200,100),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b8=Button(label4,image=self.photoimg12,cursor="hand2",relief="solid",command=self.exit_btn)
        b8.place(x=960,y=280,width=200,height=100)

        b8=Button(label4,text="EXIT",cursor="hand2",font=("lucida sans",10,"bold"),bg="purple",fg="white",relief="solid",command=self.exit_btn)
        b8.place(x=960,y=370,width=200,height=30)

    #function buttons
    def std_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)

    def face_recognition_btn(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)

    def chatbot_btn(self):
        self.new_window=Toplevel(self.root)
        self.app=chatbot(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)

    def gallery(self):
        os.startfile("gallery")

    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=developer(self.new_window)

    def exit_btn(self): 
        exit=messagebox.askyesno("Exit","Do you want to exit",parent=self.root)
        if exit>0:
            self.root.destroy()
        else:
            return
        

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
