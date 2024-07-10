from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import cv2.face
import numpy as np

class train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x810+0+0")
        self.root.title("TRAIN DATA")
        self.root.resizable(width=False,height=False)
        self.root.wm_iconbitmap("52.ico")

        #1)train data label
        label1=Label(self.root,text="TRAINING DATASET",font=("lucida sans",20,"bold"),bg="#FF5A5F",fg="white",relief="solid")
        label1.place(x=5,y=5,height=50,width=1348)

        #2)background label
        label2=Label(self.root,relief="solid",bg="#087E8B")
        label2.place(x=5,y=60,width=1348,height=660)

        #3)image 1
        img1=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\17.jpg")
        img1=img1.resize((400,300),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label3=Label(label2,image=self.photoimg1,relief="solid")
        label3.place(x=10,y=10,width=400,height=300)

        #4)image 2
        img2=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\18.jpg")
        img2=img2.resize((400,300),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label4=Label(label2,image=self.photoimg2,relief="solid")
        label4.place(x=10,y=315,width=400,height=300)

        #5)image 3
        img3=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\19.jpg")
        img3=img3.resize((500,230),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        label5=Label(label2,image=self.photoimg3,relief="solid")
        label5.place(x=420,y=10,width=500,height=230)

        #6)image 4
        img4=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\20.jpg")
        img4=img4.resize((500,235),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        label6=Label(label2,image=self.photoimg4,relief="solid")
        label6.place(x=420,y=380,width=500,height=235)

        #7)image 5
        img5=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\21.jpg")
        img5=img5.resize((405,300),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        label7=Label(label2,image=self.photoimg5,relief="solid")
        label7.place(x=930,y=10,width=405,height=300)

        #8)image 6
        img6=Image.open(r"C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\images\22.jpg")
        img6=img6.resize((405,300),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        label8=Label(label2,image=self.photoimg6,relief="solid")
        label8.place(x=930,y=315,width=405,height=300)

        #)train data button
        b1=Button(label2,text="TAP TO TRAIN DATA",font=("lucida sans",15,"bold"),bg="#FFB703",cursor="hand2",relief="solid",command=self.train_data)
        b1.place(x=420,y=255,width=500,height=110)

    def train_data(self):
        data_dir=("gallery") # for extracting data from gallery folder
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)] # The os.path.join() Method in Python joins one or more path components intelligently. This method concatenates various path components with exactly one directory separator (‘/’) following each non-empty part except the last path component.
        #The os.listdir() method in Python is used to get the list of all files and directories in the specified directory.

        faces=[]
        ids=[]

        for image in path:  # img= C:\Users\VAISHNAVI\OneDrive\Desktop\face recognition attendence system\gallery\user.1.1.jpg" for 1st iteration
            img=Image.open(image).convert('L') # for converting it into gray scale
            img_np=np.array(img,'uint8') # uint8 is datatype. it is used for converting the image into grid
            id=int(os.path.split(image)[1].split(".")[1]) # it is used for splitting the path into head and tail which can be retrieved through their index

            faces.append(img_np)
            ids.append(id)
            cv2.imshow("Training",img_np) # for displaying the image in the window
            cv2.moveWindow("Training",450,90)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #training the classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=train(root)
    root.mainloop()