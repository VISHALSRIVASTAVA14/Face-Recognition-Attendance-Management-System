from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import cv2
from time import strftime
from datetime import datetime

class face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x810+0+0")
        self.root.title("FACE RECOGNITION")
        self.root.resizable(False,False)
        self.root.wm_iconbitmap("52.ico")

        #1)heading label
        label1=Label(self.root,text="FACE RECOGNITION",font=("lucida sans",20,"bold"),bg="#023047",fg="white",relief="solid")
        label1.place(x=5,y=5,width=1348,height=60)

        #2)background label
        label2=Label(self.root,bg="#FB8500",relief="solid")
        label2.place(x=5,y=70,width=1348,height=650)

        #3)first image
        img1=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\23.jpg")
        img1=img1.resize((420,600),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label3=Label(label2,image=self.photoimg1,relief="solid")
        label3.place(x=20,y=20,width=420,height=600)

        #4)second image
        img2=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\24.jpg")
        img2=img2.resize((430,480),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label4=Label(label2,image=self.photoimg2,relief="solid")
        label4.place(x=445,y=20,width=430,height=480)

        #5)third image
        img3=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\25.jpg")
        img3=img3.resize((440,600),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        label5=Label(label2,image=self.photoimg3,relief="solid")
        label5.place(x=880,y=20,width=440,height=600)

        #6)face_detection button
        b1=Button(label2,text="FACE DETECTOR",font=("lucida sans",15,"bold"),bg="#072f5f",fg="white",cursor="hand2",relief="solid",command=self.face_detector)
        b1.place(x=445,y=500,width=430,height=120)

    #function for marking attendence
    def mark_attendence(self,e,n,d,g):
        with open("attendance_report/attendance.csv","r+",newline="\n") as f:
            my_data_list=f.readlines()
            name_list=[]

            for line in my_data_list:
                entry=line.split(",")
                name_list.append(entry[0])

            if((e not in name_list) and (n not in name_list) and (d not in name_list) and (g not in name_list)):
                now=datetime.now()
                date=now.strftime("%d/%m/%Y")
                time=now.strftime("%H:%M:%S")
                f.writelines(f"{e},{n},{d},{g},{time},{date},PRESENT\n")


    #function creation for face_recognition
    def face_detector(self):
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
    
        def draw_boundary(img,classifier,scale_factor,min_neighbour,color,text,clf):
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_img,scale_factor,min_neighbour) # used for detecting objects in the form of rectangle and stores them as list
            
            coord=[]

            for (x,y,width,height) in features:
                cv2.rectangle(img,(x,y),(x+width,y+height),(0,255,0),3) # used for drawing the rectangle on the screen with color (0,255,0) and thickness 3
                id,predict=clf.predict(gray_img[y:y+height,x:x+width]) # used for predicting the images found in the camera.it validates it with the images saved in the gallery
                confidence=int((100*(1-predict/300))) #this formula is used for recognising the accuracy of face detection

                conn=mysql.connector.connect(host="localhost",user="root",password="An@nd3009",database="face_recognition_system")
                my_cursor=conn.cursor()

                my_cursor.execute("SELECT STUDENT_NAME FROM student WHERE ENROLLMENT_NUMBER="+str(id))
                n=my_cursor.fetchone()
                n="".join(map(str,n)) if n else ""

                my_cursor.execute("SELECT ENROLLMENT_NUMBER FROM student WHERE ENROLLMENT_NUMBER="+str(id))
                e=my_cursor.fetchone()
                e="".join(map(str,e)) if e else ""

                my_cursor.execute("SELECT DEPARTMENT FROM student WHERE ENROLLMENT_NUMBER="+str(id))
                d=my_cursor.fetchone()
                d="".join(map(str,d)) if d else ""

                my_cursor.execute("SELECT GENDER FROM student WHERE ENROLLMENT_NUMBER="+str(id))
                g=my_cursor.fetchone()
                g="".join(map(str,g)) if g else ""

                if (confidence>80):
                    cv2.putText(img,f"ENROLLMENT NUMBER: {e}",(x,y-100),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2) #origin defines the position if the text. 0.8 is the scale 
                    cv2.putText(img,f"STUDENT NAME: {n}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"DEPARTMENT: {d}",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"GENDER: {g}",(x,y-25),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.mark_attendence(e,n,d,g)
                else:
                    cv2.rectangle(img,(x,y),(x+width,y+height),(0,0,255),3)
                    cv2.putText(img,"FACE NOT DETECTED",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),3)
                
                conn.close()
                coord=[x,y,width,height]
                return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        cap=cv2.VideoCapture(0)

        while True:
            ret,img=cap.read() #reads the image present in front of the camera
            img=recognize(img,clf,faceCascade)
            cv2.imshow("WELCOME TO FACE RECOGNITION",img)
            cv2.moveWindow("WELCOME TO FACE RECOGNITION",400,90)
            
            if cv2.waitKey(1)==13:
                break
        cap.release()
        cv2.destroyAllWindows()



if __name__=="__main__":
    root=Tk()
    obj=face_recognition(root)
    root.mainloop()
