from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2 # OpenCV : it a standard library for comuter vision, image proccessing and has a number of machine learning algorithms.It is used for identifying photos,images and handwritings

class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x810+0+0")
        self.root.title("Student Details")
        self.root.resizable(width=False,height=False)
        self.root.wm_iconbitmap("52.ico")

        # variables
        self.dep=StringVar()
        self.year=StringVar()
        self.sem=StringVar()
        self.enrollment=StringVar()
        self.name=StringVar()
        self.gender=StringVar()
        self.dob=StringVar()
        self.phone=StringVar()
        self.email=StringVar()
        self.class_coordinator=StringVar()
        self.radiobutton=StringVar()
        self.search_by=StringVar()
        self.search_entry=StringVar()

        #1st image
        img13=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\13.jpg")
        img13=img13.resize((450,130),Image.ANTIALIAS)
        self.photoimg13=ImageTk.PhotoImage(img13)

        label1=Label(root,image=self.photoimg13,relief="solid")
        label1.place(x=1,y=1,width=450,height=130)

        #2nd image
        img14=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\14.jpg")
        img14=img14.resize((460,130),Image.ANTIALIAS)
        self.photoimg14=ImageTk.PhotoImage(img14)

        label2=Label(root,image=self.photoimg14,relief="solid")
        label2.place(x=450,y=1,width=460,height=130)

        #3rd image
        img15=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\15.jpg")
        img15=img15.resize((460,130),Image.ANTIALIAS)
        self.photoimg15=ImageTk.PhotoImage(img15)

        label3=Label(root,image=self.photoimg15,relief="solid")
        label3.place(x=900,y=1,width=456,height=130)

        #background image
        img16=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\16.jpg")
        img16=img16.resize((1360,600),Image.ANTIALIAS)
        self.photoimg16=ImageTk.PhotoImage(img16)

        label4=Label(root,image=self.photoimg16,relief="solid")
        label4.place(x=1,y=129,width=1356,height=600)

        #heading
        label5=Label(root,text="STUDENT MANAGEMENT SYSTEM",font=("luciad sans",15,"bold"),fg="black",bg="#FAD6A5",width=35,height=2,relief="solid")
        label5.place(x=460,y=125)

        #frame
        frame1=Frame(label4,bd=2)
        frame1.place(x=35,y=35,width=1290,height=520)

        #left frame
        labelframe1=LabelFrame(frame1,text="STUDENT DETAILS",bd=2,relief="solid",font=("lucida sans",10,"bold"))
        labelframe1.place(x=10,y=10,width=600,height=500)

        #first label frame inside left label frame
        labelframe3=LabelFrame(labelframe1,bd=2,relief="solid",bg="#FAD6A5")
        labelframe3.place(x=4,y=5,width=588,height=100)

        #1)department
        label6=Label(labelframe3,text="DEPARTMENT",font=("lucida sans",13,"bold"))
        label6.place(x=10,y=10)

        combobox1=ttk.Combobox(labelframe3,font=("lucida sans",13,"bold"),state="readonly",textvariable=self.dep)
        combobox1["values"]=["SELECT DEPARTMENT","BCA","BBA","MBA","B.COM"]
        combobox1.current(0) #SELECT DEPARTMENT WILL BE BY DEFAULT
        combobox1.place(x=150,y=10)

        #2)year
        label7=Label(labelframe3,text="YEAR",font=("lucida sans",13,"bold"))
        label7.place(x=10,y=50)
        
        combobox2=ttk.Combobox(labelframe3,font=("lucida sans",10,"bold"),state="readonly",textvariable=self.year)
        combobox2["values"]=["SELECT YEAR","I","II","III"]
        combobox2.current(0)
        combobox2.place(x=70,y=52,width=130)

        #3)semester
        label8=Label(labelframe3,text="SEMESTER",font=("lucida sans",13,"bold"))
        label8.place(x=300,y=50)

        combobox3=ttk.Combobox(labelframe3,font=("lucida sans",10,"bold"),state="readonly",textvariable=self.sem)
        combobox3["values"]=["SELECT SEMESTER","I","II","III","IV","V","VI"]
        combobox3.current(0)
        combobox3.place(x=410,y=52,width=150)

        #second labelframe inside left labelframe
        labelframe4=LabelFrame(labelframe1,bd=2,relief="solid",bg="#FAD6A5")
        labelframe4.place(x=4,y=110,width=588,height=360)

        #4)enrollment number
        label9=Label(labelframe4,text="ENROLLMENT NUMBER",font=("lucida sans",12,"bold"))
        label9.place(x=10,y=10)

        entry1=ttk.Entry(labelframe4,font=("lucida sans",10,"bold"),textvariable=self.enrollment)
        entry1.place(x=250,y=11,width=320,height=22)

        #5)student name
        label10=Label(labelframe4,text="STUDENT NAME",font=("lucida sans",12,"bold"))
        label10.place(x=10,y=40,width=205,height=22)

        entry2=ttk.Entry(labelframe4,font=("lucida sans",10,"bold"),textvariable=self.name)
        entry2.place(x=250,y=40,width=320,height=22)

        #6)gender
        label11=Label(labelframe4,text="GENDER",font=("lucida sans",12,"bold"))
        label11.place(x=10,y=69,width=205,height=22)

        combobox5=ttk.Combobox(labelframe4,font=("lucida sans",10,"bold"),state="readonly",textvariable=self.gender)
        combobox5["values"]=["SELECT GENDER","MALE","FEMALE","OTHERS"]
        combobox5.current(0)
        combobox5.place(x=250,y=69,width=320,height=22)

        #7)dob
        label12=Label(labelframe4,text="D.O.B",font=("lucida sans",12,"bold"))
        label12.place(x=10,y=98,width=205,height=22)

        entry4=ttk.Entry(labelframe4,font=("lucida sans",10,"bold"),textvariable=self.dob)
        entry4.place(x=250,y=98,width=320,height=22)

        #9)phone number
        label13=Label(labelframe4,text="PHONE NUMBER",font=("lucida sans",12,"bold"))
        label13.place(x=10,y=127,width=205,height=22)

        entry5=ttk.Entry(labelframe4,font=("lucida sans",10,"bold"),textvariable=self.phone)
        entry5.place(x=250,y=127,width=320,height=22)

        #10)e-mail
        label14=Label(labelframe4,text="E-MAIL",font=("lucida sans",12,"bold"))
        label14.place(x=10,y=156,width=205,height=22)

        entry6=ttk.Entry(labelframe4,font=("lucida sans",10,"bold"),textvariable=self.email)
        entry6.place(x=250,y=156,width=320,height=22)

        #11)class coordinator name
        label15=Label(labelframe4,text="CLASS COORDINATOR",font=("lucida sans",12,"bold"))
        label15.place(x=10,y=185,width=205,height=22)

        entry7=ttk.Entry(labelframe4,font=("lucida sans",10,"bold"),textvariable=self.class_coordinator)
        entry7.place(x=250,y=185,width=320,height=22)

        #12)radiobutton1
        radiobtn1=ttk.Radiobutton(labelframe4,text="TAKE A PHOTO SAMPLE",value="YES",variable=self.radiobutton)
        radiobtn1.place(x=10,y=220,width=205,height=22)

        #13)radiobutton2
        radiobtn2=ttk.Radiobutton(labelframe4,text="NO SAMPLE PHOTO",value="NO",variable=self.radiobutton)
        radiobtn2.place(x=250,y=220,width=320,height=22)

        #14)save button
        b1=Button(labelframe4,text="SAVE",font=("lucida sans",12,"bold"),bg="#28282B",fg="white",cursor="hand2",command=self.add_data)
        b1.place(x=10,y=260,width=140)

        #15)update button
        b2=Button(labelframe4,text="UPDATE",font=("lucida sans",12,"bold"),bg="#28282B",fg="white",cursor="hand2",command=self.update)
        b2.place(x=150,y=260,width=140)

        #16)delete button
        b3=Button(labelframe4,text="DELETE",font=("lucida sans",12,"bold"),bg="#28282B",fg="white",cursor="hand2",command=self.delete_data)
        b3.place(x=290,y=260,width=140)

        #17)reset button
        b4=Button(labelframe4,text="RESET",font=("lucida sans",12,"bold"),bg="#28282B",fg="white",cursor="hand2",command=self.reset_fields)
        b4.place(x=430,y=260,width=140)

        #18)take photo sample button
        b5=Button(labelframe4,text="TAKE A SAMPLE PHOTO",font=("lucida sans",12,"bold"),bg="#28282B",fg="white",cursor="hand2",command=self.taking_photo_sample)
        b5.place(x=10,y=292,width=560,height=40)

        #right frame
        labelframe2=LabelFrame(frame1,text="STUDENT INFORMATION",bd=2,relief="solid",font=("lucida sans",10,"bold"))
        labelframe2.place(x=615,y=10,width=660,height=500)
        
        #first label frame inside right label frame
        labelframe5=LabelFrame(labelframe2,bd=2,relief="solid",bg="#FAD6A5")
        labelframe5.place(x=5,y=5,width=645,height=80)

        #1)search section
        label16=Label(labelframe5,text="SEARCH BY",font=("lucida sans",12,"bold"))
        label16.place(x=10,y=20)

        combobox4=ttk.Combobox(labelframe5,font=("lucida sans",10,"bold"),state="readonly",textvariable=self.search_by)
        combobox4["values"]=["SELECT","ENROLLMENT NUMBER","PHONE NUMBER"]
        combobox4.current(0)
        combobox4.place(x=120,y=21,width=130)

        #2)search entry
        entry8=ttk.Entry(labelframe5,font=("lucida sans",10,"bold"),textvariable=self.search_entry)
        entry8.place(x=260,y=21,width=150,height=22)

        #3)search button
        b7=Button(labelframe5,text="SEARCH",font=("lucida sans",10,"bold"),bg="#28282B",fg="white",cursor="hand2",command=self.search_btn)
        b7.place(x=430,y=18,width=80)

        #4)showall button
        b8=Button(labelframe5,text="SHOW ALL",font=("lucida sans",10,"bold"),bg="#28282B",fg="white",cursor="hand2",command=self.fetch_data)
        b8.place(x=520,y=18,width=80)

        #frame inside right label frame
        frame2=Frame(labelframe2,bg="#FAD6A5",bd=2,relief="solid")
        frame2.place(x=5,y=90,width=645,height=380)

        #5)scrollbar
        scroll_x=ttk.Scrollbar(frame2,orient="horizontal")
        scroll_y=ttk.Scrollbar(frame2,orient="vertical")

        # CREATING TABLE USING Treeview function 

        self.student_table=ttk.Treeview(frame2,column=("DEP","YEAR","SEMESTER","ENROLLMENT NUMBER","NAME","GENDER","DOB","PHONE NUMBER","E-MAIL","CLASS COORDINATOR","PHOTO SAMPLE"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side="bottom",fill="x")
        scroll_y.pack(side="right",fill="y")
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("DEP",text="DEPARTMENT")
        self.student_table.heading("YEAR",text="YEAR")
        self.student_table.heading("SEMESTER",text="SEMESTER")
        self.student_table.heading("ENROLLMENT NUMBER",text="ENROLLMENT NUMBER")
        self.student_table.heading("NAME",text="STUDENT NAME")
        self.student_table.heading("GENDER",text="GENDER")
        self.student_table.heading("DOB",text="D.O.B")
        self.student_table.heading("PHONE NUMBER",text="PHONE NUMBER")
        self.student_table.heading("E-MAIL",text="E-MAIL")
        self.student_table.heading("CLASS COORDINATOR",text="CLASS COORDINATOR")
        self.student_table.heading("PHOTO SAMPLE",text="PHOTO SAMPLE")

        self.student_table["show"]="headings"
        
        self.student_table.column("DEP",width=150)
        self.student_table.column("YEAR",width=150)
        self.student_table.column("SEMESTER",width=150)
        self.student_table.column("ENROLLMENT NUMBER",width=150)
        self.student_table.column("NAME",width=250)
        self.student_table.column("GENDER",width=150)
        self.student_table.column("DOB",width=150)
        self.student_table.column("PHONE NUMBER",width=150)
        self.student_table.column("E-MAIL",width=150)
        self.student_table.column("CLASS COORDINATOR",width=150)
        self.student_table.column("PHOTO SAMPLE",width=150)

        self.student_table.pack(fill="both",expand=1)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data() # previous details of the database will be displayed

    #function declaration
    def add_data(self):
        if (self.dep.get()=="SELECT DEPARTMENT" or self.year.get()=="SELECT YEAR" or self.sem.get()=="SELECT SEMESTER" or self.enrollment.get()=="" or self.name.get()=="" or self.gender.get()=="SELECT GENDER" or self.dob.get()=="" or self.phone.get()=="" or self.email.get()=="" or self.class_coordinator.get()=="" or self.radiobutton.get()==""):
            messagebox.showerror("Error","All fields are required to be filled",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="An@nd3009",database="face_recognition_system")
                
                #for performing query on database we use cursor 
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.dep.get(),self.year.get(),self.sem.get(),self.enrollment.get(),self.name.get(),self.gender.get(),self.dob.get(),self.phone.get(),self.email.get(),self.class_coordinator.get(),self.radiobutton.get()))
                
                conn.commit() #it wil update the table from time to time

                self.fetch_data() #it will display the result in right frame
                
                conn.close()
                messagebox.showinfo("Success","Details added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #fetching data from the database on the right frame
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="An@nd3009",database="face_recognition_system")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data=my_cursor.fetchall() #This method fetches all  rows of a query result set and returns a list of tuples. If no more rows are available, it returns an empty list.

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #for updating the values when clicked on the data present in the table
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.dep.set(data[0])
        self.year.set(data[1])
        self.sem.set(data[2])
        self.enrollment.set(data[3])
        self.name.set(data[4])
        self.gender.set(data[5])
        self.dob.set(data[6])
        self.phone.set(data[7])
        self.email.set(data[8])
        self.class_coordinator.set(data[9])
        self.radiobutton.set(data[10])
    
    #update function
    def update(self):
        if(self.dep.get()=="" or self.year.get()=="" or self.sem.get()=="" or self.enrollment.get()=="" or self.name.get()=="" or self.gender.get()=="SELECT GENDER" or self.dob.get()=="" or self.phone.get()=="" or self.email.get()=="" or self.class_coordinator.get()=="" or self.radiobutton.get==""):
            messagebox.showerror("Error","All fields are required to be filled",parent=self.root)
        else:
            try:
                update_var=messagebox.askyesno("Update","Do you want to update the details",parent=self.root)
                if(update_var>0):
                    conn=mysql.connector.connect(host="localhost",user="root",password="An@nd3009",database="face_recognition_system")
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE student SET DEPARTMENT=%s,YEAR=%s,SEMESTER=%s,ENROLLMENT_NUMBER=%s,STUDENT_NAME=%s,GENDER=%s,DOB=%s,PHONE_NUMBER=%s,E_MAIL=%s,CLASS_COORDINATOR=%s,PHOTO_SAMPLE=%s WHERE ENROLLMENT_NUMBER=%s",(self.dep.get(),self.year.get(),self.sem.get(),self.enrollment.get(),self.name.get(),self.gender.get(),self.dob.get(),self.phone.get(),self.email.get(),self.class_coordinator.get(),self.radiobutton.get(),self.enrollment.get()))
                    conn.commit()
                    conn.close()    
                    self.fetch_data()
                else:
                    if not update_var:
                        return
                messagebox.showinfo("Success","Details updated successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.enrollment.get()=="":
            messagebox.showerror("Error","Please fill the enrollment number",parent=self.root)
        else:
            try:
                delete_var=messagebox.askyesno("Delete","Do you want to delete the data",parent=self.root)
                if(delete_var>0):
                    conn=mysql.connector.connect(host="localhost",user="root",password="An@nd3009",database="face_recognition_system")
                    my_cursor=conn.cursor()
                    my_cursor.execute("DELETE FROM student WHERE ENROLLMENT_NUMBER=%s",(self.enrollment.get(),))
                else:
                    if not delete_var:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted data",parent=self.root)
                self.reset_fields()
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)
    
    #reset function
    def reset_fields(self):
        self.dep.set("SELECT DEPARTMENT")
        self.year.set("SELECT YEAR")
        self.sem.set("SELECT SEMESTER")
        self.enrollment.set("")
        self.name.set("")
        self.gender.set("SELECT GENDER")
        self.dob.set("")
        self.phone.set("")
        self.email.set("")
        self.class_coordinator.set("")
        self.radiobutton.set("")
    
    #taking_photo_sample function using OpenCV(Generating photo samples)
    def taking_photo_sample(self):
        if(self.dep.get()=="SELECT DEPARTMENT" or self.year.get()=="SELECT YEAR" or self.sem.get()=="SELECT SEMESTER" or self.enrollment.get()=="" or self.name.get()=="" or self.gender.get()=="SELECT GENDER" or self.dob.get()=="" or self.phone.get()=="" or self.email.get()=="" or self.class_coordinator.get()=="" or self.radiobutton.get()==""):
            messagebox.showerror("Error","All fields must be filled",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="An@nd3009",database="face_recognition_system")
                my_cursor=conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                data=my_cursor.fetchall() # fetches data as a list of tuples
                id=0
                for i in data:
                    id=id+1
                
                my_cursor.execute("UPDATE student SET DEPARTMENT=%s,YEAR=%s,SEMESTER=%s,ENROLLMENT_NUMBER=%s,STUDENT_NAME=%s,GENDER=%s,DOB=%s,PHONE_NUMBER=%s,E_MAIL=%s,CLASS_COORDINATOR=%s,PHOTO_SAMPLE=%s WHERE ENROLLMENT_NUMBER=%s",(self.dep.get(),self.year.get(),self.sem.get(),self.enrollment.get(),self.name.get(),self.gender.get(),self.dob.get(),self.phone.get(),self.email.get(),self.class_coordinator.get(),self.radiobutton.get(),self.enrollment.get()==id+1))
                conn.commit()
                self.fetch_data()
                self.reset_fields()
                conn.close()

                #load predefined data on face from haarcascade_frontalface_default algoritm of OpenCV
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # it is used for converting the coloured images to gray(i.e black and white)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)  #gray is image and scaling factor=1.3 and minimum neighbour =5 and is used for dtetecting objects of different sizes present in the image, the detected objects are returned as a list of rectangles

                    for (a,b,width,height) in faces:
                        face_croped=img[b:b+width,a:a+height]
                        return face_croped
                    
                cap=cv2.VideoCapture(0) # it will open the front camera
                img_id=0

                while True:
                    ret,my_frame=cap.read() # the read() method is used to read the frames using the above created object(i.e. cap).
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="gallery/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face) # (filename,image)

                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),3) # cv2.putText() method is used to draw a text string on any image.(50,50) is origin, 2 is the font scale,(0,255,0) is font color and 3 is the thickness
                        
                        cv2.imshow("Cropped faces:",face) # cv2.imshow() method is used to display an image in a window.(window_name, image)
                        
                        cv2.moveWindow("Cropped faces:",450,90)

                    if cv2.waitKey(1)==13 or int(img_id)==100: # waitKey() is used for displaying a window for some miliseconds and if 0 is passed as a parameter then it will be displayed untill any key is pressed
                        break
                
                cap.release()
                cv2.destroyWindow("Cropped faces:")
                messagebox.showinfo("Result","Generated data set is completed")

            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)
            
    def search_btn(self):
        if (self.search_by.get()=="SELECT" or self.search_entry.get()==""):
            messagebox.showerror("Error","All entries must be filled for searching",parent=self.root)
        else:
            if self.search_by.get()=="ENROLLMENT NUMBER":
                try:
                    conn=mysql.connector.connect(host="localhost",user="root",password="An@nd3009",database="face_recognition_system")
                    my_cursor=conn.cursor()

                    my_cursor.execute("SELECT * FROM student WHERE ENROLLMENT_NUMBER=%s",(self.search_entry.get(),))
                    data=my_cursor.fetchall()

                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                    conn.close()
                
                except Exception as es:
                    messagebox.showerror("Error",f"Due to : str{es}",parent=self.root)
            
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",user="root",password="An@nd3009",database="face_recognition_system")
                    my_cursor=conn.cursor()

                    my_cursor.execute("SELECT * FROM student WHERE PHONE_NUMBER=%s",(self.search_entry.get(),))
                    data=my_cursor.fetchall()

                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error",f"Due to : str{es}",parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj2=student(root)
    root.mainloop()

