from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

class developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x810+0+0")
        self.root.title("DEVELOPER")
        self.root.resizable(False,False)
        self.root.wm_iconbitmap("52.ico")

        #left label
        label1=Label(self.root,bg="#023246",relief="solid")
        label1.place(x=5,y=5,width=402,height=725)

        #image in left label
        img1=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\30.jpeg")
        img1=img1.resize((388,410),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label11=Label(label1,image=self.photoimg1,relief="solid")
        label11.place(x=5,y=5,width=388,height=410)

        #description labels
        label12=Label(label1,text="SUMMARY",font=("lucida sans",15,"bold"),bg="#287094",fg="white",relief="solid")
        label12.place(x=5,y=420,width=388,height=50)

        label13=Label(label1,fg="black",bg="#F6F6F6",relief="solid",text="HELLO!!!!, I AM VISHAL SRIVASTAVA \nI AM AN ENTHUSIASTIC BCA STUDENT WITH \nSTRONG FOUNDATION IN COMPUTER SCIENCE \nPRINCIPLES AND POSSESS INTEREST IN VARIOUS \n PROGRAMMING LANGUAGES. I POSSESS THE \nABILITY TO COLLABORATE EFFECTIEVELY \nIN TEAM SETTINGS AND HAS A KEEN \nINTEREST IN LEARNING NEW TECHNOLOGIES. ",font=("lucida sans",11,"bold"))
        label13.place(x=5,y=465,width=388,height=250)


        #right label
        label2=Label(self.root,bg="#D4D4CE",relief="solid")
        label2.place(x=405,y=5,width=948,height=725)

        #contact label
        label3=Label(label2,text="CONTACT",font=("lucida sans",15,"bold"),bg="#287094",fg="white",relief="solid")
        label3.place(x=5,y=5,width=450,height=50)

        label4=Label(label2,bg="WHITE",relief="solid")
        label4.place(x=5,y=53,width=450,height=208)

        #1)phone number label
        img2=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\31.jpg")
        img2=img2.resize((40,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        phn_img=Label(label4,image=self.photoimg2)
        phn_img.place(x=40,y=20,width=40,height=40)

        phn_text_label=Label(label4,text="+91 9696665671",font=("lucida sans",13,"bold"),bg="white")
        phn_text_label.place(x=80,y=25,width=200,height=30)

        #2)email label
        img3=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\32.jpg")
        img3=img3.resize((40,40),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        email_img=Label(label4,image=self.photoimg3)
        email_img.place(x=40,y=70,width=40,height=40)

        email_text_label=Label(label4,text="vishal14022004@gmail.com",font=("lucida sans",13,"bold"),bg="white")
        email_text_label.place(x=80,y=70,width=300,height=30)
        
        #3)linedin label
        img4=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\33.jpg")
        img4=img4.resize((45,45),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        linkedin_img=Label(label4,image=self.photoimg4)
        linkedin_img.place(x=40,y=120,width=45,height=45)

        linkedin_text_label=Label(label4,text="https://www.linkedin.com/in\n/vishal-srivastava-45954a2a3",font=("lucida sans",13,"bold"),bg="white")
        linkedin_text_label.place(x=100,y=110,width=270,height=60)

        #education label
        label5=Label(label2,text="EDUCATION",font=("lucida sans",15,"bold"),bg="#287094",fg="white",relief="solid")
        label5.place(x=5,y=268,width=450,height=50)

        label6=Label(label2,bg="white",relief="solid")
        label6.place(x=5,y=315,width=450,height=400)

        #1)msi label
        img5=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\34.jfif")
        img5=img5.resize((60,60),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        msi_label=Label(label6,image=self.photoimg5,relief="groove")
        msi_label.place(x=20,y=20,width=60,height=60)

        msi_text_label=Label(label6,text="(2022-2025) - COMPLETED BACHELOR OF\nCOMPUTER APPLICATIONS FROM \nMAHARAJA SURAJMAL INSTITUTE \nWITH 9.56 CGPA",font=("lucida sans",12,"bold"),bg="white")
        msi_text_label.place(x=80,y=20,width=350,height=80)

        #2)rlb label
        img6=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\35.png")
        img6=img6.resize((60,60),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        rlb_label=Label(label6,image=self.photoimg6,relief="groove")
        rlb_label.place(x=20,y=150,width=60,height=60)

        rlb_text_label=Label(label6,text="(2022) - COMPLETED SENIOR \nSECONDARY EDUCATION FROM RANI\nLAXMI BAI MEMORIAL \nSCHOOL WITH 95.2% AGGREGATE",font=("lucida sans",12,"bold"),bg="white")
        rlb_text_label.place(x=80,y=140,width=350,height=80)

        #3)rlb label
        img7=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\35.png")
        img7=img7.resize((60,60),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        rlb_label2=Label(label6,image=self.photoimg7,relief="groove")
        rlb_label2.place(x=20,y=270,width=60,height=60)

        rlb_text_label2=Label(label6,text="(2020) - COMPLETED MARTICULATION \nFROM RANI LAXMI BAI \nMEMORIAL SCHOOL WITH 93.2% \nAGGREGATE",font=("lucida sans",12,"bold"),bg="white")
        rlb_text_label2.place(x=80,y=260,width=350,height=100)


        #interests label
        label7=Label(label2,text="INTERESTS",font=("lucida sans",15,"bold"),bg="#287094",fg="white",relief="solid")
        label7.place(x=460,y=5,width=478,height=50)

        label8=Label(label2,bg="white",relief="solid")
        label8.place(x=460,y=52,width=478,height=303)

        #1)badminton 
        img8=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\36.jpg")
        img8=img8.resize((130,130),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        badminton_label=Label(label8,image=self.photoimg8,relief="groove")
        badminton_label.place(x=20,y=15,width=130,height=130)

        #2)coding
        img9=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\37.jpg")
        img9=img9.resize((130,130),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        coding_label=Label(label8,image=self.photoimg9,relief="groove")
        coding_label.place(x=173,y=15,width=130,height=130)

        #3)cricket
        img10=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\38.jpg")
        img10=img10.resize((130,130),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        cricket_label=Label(label8,image=self.photoimg10,relief="groove")
        cricket_label.place(x=325,y=15,width=130,height=130)

        #4)workout
        img11=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\39.jpg")
        img11=img11.resize((130,130),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        workout_label=Label(label8,image=self.photoimg11,relief="groove")
        workout_label.place(x=95,y=155,width=130,height=130)

        #5)gaming
        img12=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\40.jpg")
        img12=img12.resize((130,130),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        gaming_label=Label(label8,image=self.photoimg12,relief="groove")
        gaming_label.place(x=245,y=155,width=130,height=130)


        #skills label
        label9=Label(label2,text="SKILLS",font=("lucida sans",15,"bold"),bg="#287094",fg="white",relief="solid")
        label9.place(x=460,y=363,width=478,height=50)

        label10=Label(label2,bg="white",relief="solid")
        label10.place(x=460,y=410,width=478,height=304)

        #1)c++
        img13=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\41.png")
        img13=img13.resize((130,130),Image.ANTIALIAS)
        self.photoimg13=ImageTk.PhotoImage(img13)

        cpp_label=Label(label10,image=self.photoimg13,relief="groove")
        cpp_label.place(x=20,y=15,width=130,height=130)

        #2)java
        img14=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\42.png")
        img14=img14.resize((140,130),Image.ANTIALIAS)
        self.photoimg14=ImageTk.PhotoImage(img14)

        java_label=Label(label10,image=self.photoimg14,relief="groove")
        java_label.place(x=173,y=15,width=140,height=130)

        #3)python
        img15=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\43.png")
        img15=img15.resize((130,130),Image.ANTIALIAS)
        self.photoimg15=ImageTk.PhotoImage(img15)

        python_label=Label(label10,image=self.photoimg15,relief="groove")
        python_label.place(x=325,y=15,width=130,height=130)

        #4)php
        img16=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\44.png")
        img16=img16.resize((130,130),Image.ANTIALIAS)
        self.photoimg16=ImageTk.PhotoImage(img16)

        php_label=Label(label10,image=self.photoimg16,relief="groove")
        php_label.place(x=95,y=155,width=130,height=130)
        
        #5)sql
        img17=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\45.png")
        img17=img17.resize((130,130),Image.ANTIALIAS)
        self.photoimg17=ImageTk.PhotoImage(img17)

        sql_label=Label(label10,image=self.photoimg17,relief="groove")
        sql_label.place(x=245,y=155,width=130,height=130)


if __name__=="__main__":
    root=Tk()
    obj=developer(root)
    root.mainloop()
