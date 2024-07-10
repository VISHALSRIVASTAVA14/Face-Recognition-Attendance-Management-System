from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import os
import csv
from tkinter import filedialog

my_data=[]
class attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x810+0+0")
        self.root.title("ATTENDANCE MANAGEMENT SYSTEM")
        self.root.resizable(False,False)
        self.root.wm_iconbitmap("52.ico")

        self.enrollment=StringVar()
        self.name=StringVar()
        self.dep=StringVar()
        self.gender=StringVar()
        self.time=StringVar()
        self.date=StringVar()
        self.status=StringVar()

        #1)image 1
        img1=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\26.jpg")
        img1=img1.resize((450,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label1=Label(self.root,image=self.photoimg1,relief="solid")
        label1.place(x=2,y=2,width=450,height=200)

        #2)image 2
        img2=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\28.jpg")
        img2=img2.resize((450,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label2=Label(self.root,image=self.photoimg2,relief="solid")
        label2.place(x=450,y=2,width=450,height=200)

        #3)imgae 3
        img3=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\27.png")
        img3=img3.resize((455,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        label3=Label(self.root,image=self.photoimg3,relief="solid")
        label3.place(x=898,y=2,width=458,height=200)

        #4)background label
        label4=Label(self.root,bg="#FCCB06",relief="solid")
        label4.place(x=2,y=200,width=1354,height=530)

        #5)heading label
        label5=Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font=("lucida sans",20,"bold"),bg="#222E50",fg="White",relief="solid")
        label5.place(x=380,y=185,width=600,height=50)

        #6)labelframe left
        labelframe1=LabelFrame(label4,text="STUDENT DETAILS",bg="#EDF7F6",relief="solid")
        labelframe1.place(x=10,y=15,width=600,height=500)

        #7)labelframe right
        labelframe2=Label(label4,bg="#EDF7F6",relief="solid")
        labelframe2.place(x=613,y=15,width=725,height=500)

        #8)enrollment_number entry
        label6=Label(labelframe1,text="ENROLLMENT NUMBER",font=("lucida sans",12,"bold"),bg="#6F8695")
        label6.place(x=30,y=30,width=250,height=25)

        entry1=ttk.Entry(labelframe1,font=("lucida sans",12,"bold"),textvariable=self.enrollment)
        entry1.place(x=310,y=30,width=260,height=25)

        #9)student name entry
        label7=Label(labelframe1,text="STUDENT NAME",font=("lucida sans",12,"bold"),bg="#6F8695")
        label7.place(x=30,y=70,width=250,height=25)

        entry2=ttk.Entry(labelframe1,font=("lucida sans",12,"bold"),textvariable=self.name)
        entry2.place(x=310,y=70,width=260,height=25)

        #10)department name entry
        label8=Label(labelframe1,text="DEPARTMENT",font=("lucida sans",12,"bold"),bg="#6F8695")
        label8.place(x=30,y=110,width=250,height=25)

        combobox3=ttk.Combobox(labelframe1,font=("lucida sans",12,"bold"),textvariable=self.dep,state="readonly")
        combobox3["values"]=["SELECT DEPARTMENT","BCA","BBA","B.COM","MBA"]
        combobox3.current(0)
        combobox3.place(x=310,y=110,width=260,height=25)

        #11)gender combobox
        label9=Label(labelframe1,text="GENDER",font=("lucida sans",12,"bold"),bg="#6F8695")
        label9.place(x=30,y=150,width=250,height=25)

        combobox1=ttk.Combobox(labelframe1,font=("lucida sans",12,"bold"),textvariable=self.gender,state="readonly")
        combobox1["values"]=["SELECT GENDER","MALE","FEMALE"]
        combobox1.current(0)
        combobox1.place(x=310,y=150,width=260,height=25)

        #12)time entry
        label10=Label(labelframe1,text="TIME",font=("lucida sans",12,"bold"),bg="#6F8695")
        label10.place(x=30,y=190,width=250,height=25)

        entry4=ttk.Entry(labelframe1,font=("lucida sans",12,"bold"),textvariable=self.time)
        entry4.place(x=310,y=190,width=260,height=25)

        #13)date entry
        label11=Label(labelframe1,text="DATE",font=("lucida sans",12,"bold"),bg="#6F8695")
        label11.place(x=30,y=230,width=250,height=25)

        entry5=ttk.Entry(labelframe1,font=("lucida sans",12,"bold"),textvariable=self.date)
        entry5.place(x=310,y=230,width=260,height=25)

        #14)attendance status combobox
        label12=Label(labelframe1,text="ATTENDANCE STATUS",font=("lucida sans",12,"bold"),bg="#6F8695")
        label12.place(x=30,y=270,width=250,height=25)

        combobox2=ttk.Combobox(labelframe1,font=("lucida sans",12,"bold"),textvariable=self.status,state="readonly")
        combobox2["values"]=["STATUS","PRESENT","ABSENT"]
        combobox2.current(0)
        combobox2.place(x=310,y=270,width=260,height=25)

        #15)import csv button
        b1=Button(labelframe1,text="IMPORT CSV",font=("lucida sans",16,"bold"),bg="#262525",fg="white",cursor="hand2",command=self.import_csv)
        b1.place(x=30,y=330,width=269,height=60)

        #16)export csv button
        b2=Button(labelframe1,text="EXPORT CSV",font=("lucida sans",16,"bold"),bg="#262525",fg="white",cursor="hand2",command=self.export_csv)
        b2.place(x=300,y=330,width=269,height=60)

        #17)update button
        b3=Button(labelframe1,text="UPDATE",font=("lucida sans",16,"bold"),bg="#262525",fg="white",cursor="hand2",command=self.update)
        b3.place(x=30,y=391,width=269,height=60)

        #18)reset button
        b4=Button(labelframe1,text="RESET",font=("lucida sans",16,"bold"),bg="#262525",fg="white",cursor="hand2",command=self.reset)
        b4.place(x=300,y=391,width=269,height=60)

        #19)table in the rigt label frame

        frame1=Frame(labelframe2)
        frame1.place(x=20,y=30,width=680,height=450)
        
        #scrollbar creation
        scroll_x=ttk.Scrollbar(frame1,orient="horizontal")
        scroll_y=ttk.Scrollbar(frame1,orient="vertical")

        #creating table

        self.attendance_table=ttk.Treeview(frame1,columns=("ENROLLMENT NUMBER","STUDENT NAME","DEPARTMENT","GENDER","TIME","DATE","ATTENDANCE STATUS"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side="bottom",fill="x")
        scroll_y.pack(side="right",fill="y")
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("ENROLLMENT NUMBER",text="ENROLLMENT NUMBER")
        self.attendance_table.heading("STUDENT NAME",text="STUDENT NAME")
        self.attendance_table.heading("DEPARTMENT",text="DEPARTMENT")
        self.attendance_table.heading("GENDER",text="GENDER")
        self.attendance_table.heading("TIME",text="TIME")
        self.attendance_table.heading("DATE",text="DATE")
        self.attendance_table.heading("ATTENDANCE STATUS",text="ATTENDANCE STATUS")

        self.attendance_table["show"]="headings"

        self.attendance_table.column("ENROLLMENT NUMBER",width=200)
        self.attendance_table.column("STUDENT NAME",width=250)
        self.attendance_table.column("DEPARTMENT",width=200)
        self.attendance_table.column("GENDER",width=200)
        self.attendance_table.column("TIME",width=200)
        self.attendance_table.column("DATE",width=200)
        self.attendance_table.column("ATTENDANCE STATUS",width=200)

        self.attendance_table.pack(fill="both",expand=1)

        self.attendance_table.bind("<ButtonRelease>",self.get_cursor)

    #function for fetching the data 
    def fetch_data(self,rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END,values=i)

    #function for importing csv
    def import_csv(self):
        global my_data
        my_data.clear() 
        fname=filedialog.askopenfilename(initialdir=os.getcwd,title="OPEN CSV",filetypes=(("CSV FILE","*.csv"),("ALL FILE","*.*")),parent=self.root)   #cwd is current working directory
        with open(fname) as myfile:
            csv_read=csv.reader(myfile,delimiter=",")
            for i in csv_read:
                my_data.append(i)
        self.fetch_data(my_data)

    #function for export csv
    def export_csv(self):
        try:
            if len(my_data)<1:
                messagebox.showerror("Error","No data found to export",parent=self.root)
                return False
            else:
                fname=filedialog.asksaveasfilename(initialdir=os.getcwd,title="SAVE CSV",filetypes=(("CSV FILE","*.csv"),("ALL FILE","*.*")),parent=self.root)
                with open(fname,mode="w",newline="\n") as myfile:
                    exp_write=csv.writer(myfile,delimiter=",")
                    for i in my_data:
                        exp_write.writerow(i)
                    messagebox.showinfo("Data Exported","Your data exported successfully to "+os.path.basename(fname)+"!!!",parent=self.root) 
        except Exception as es:
            messagebox.showerror("Error",f"Due to : str{es}",parent=self.root)

    #function for inserting the variables in the entries from the table
    def get_cursor(self,event=""):
        focus_cursor=self.attendance_table.focus()
        content=self.attendance_table.item(focus_cursor)
        data=content["values"]

        self.enrollment.set(data[0])
        self.name.set(data[1])
        self.dep.set(data[2])
        self.gender.set(data[3])
        self.time.set(data[4])
        self.date.set(data[5])
        self.status.set(data[6])
    
    #function for updating the attendance
    def update(self):
        if(self.enrollment.get()=="" or self.name.get()=="" or self.dep.get()=="SELECT DEPARTMENT" or self.gender.get()=="SELECT GENDER" or self.time.get()=="" or self.date.get()=="" or self.status.get()=="STATUS"):
            messagebox.showerror("Error","ALL entries must be filled for updation",parent=self.root)
        else:
            fname=filedialog.asksaveasfilename(initialdir=os.getcwd,title="UPDATE CSV",filetypes=(("CSV FILE","*.csv"),("ALL FILE","*.*")))
            global my_data
            my_data.clear()
            if fname:
                try:
                    with open(fname) as myfile:    #for reading the content of selected file
                        csv_read=csv.reader(myfile,delimiter=",")
                        for i in csv_read:
                            my_data.append(i)

                    updated=False
                    for i,row in enumerate(my_data):  #index,value is represented by i,row
                        if(row[0]==self.enrollment.get()):
                            my_data[i]=[self.enrollment.get(),self.name.get(),self.dep.get(),self.gender.get(),self.time.get(),self.date.get(),self.status.get()]
                            updated=True
                            break
                    
                    if (updated==False):
                        messagebox.showerror("Error","Enrollment number not found",parent=self.root)
                    
                    else:
                        with open(fname,"w",newline="\n") as myfile:
                            csv_write=csv.writer(myfile,delimiter=",")
                            csv_write.writerows(my_data)
                            messagebox.showinfo("Success","Data updated successfully",parent=self.root)
                            self.fetch_data(my_data)
                
                except Exception as es:
                    messagebox.showerror("Error",f"Due to : str{es}",parent=self.root)
                
            
    #reset function
    def reset(self):
        self.enrollment.set("")
        self.name.set("")
        self.dep.set("SELECT DEPARTMENT")
        self.gender.set("SELECT GENDER")
        self.time.set("")
        self.date.set("")
        self.status.set("STATUS")


if __name__=="__main__":
    root=Tk()
    obj=attendance(root)
    root.mainloop()