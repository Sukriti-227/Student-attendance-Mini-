from tkinter import*    # it is use for making GUI interface
from tkinter import ttk     #it is use for styleing
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

# making a student class
class Train:
  # making a constructor
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Face Recognition System")
        
        
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",30,"bold"),bg="lightgreen",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top = Image.open(r"C:\minproject image\Screenshot 2024-12-07 200259.png")
        img_top=img_top.resize((1530,355))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=46,width=1530,height=355)
        
                
        img_middle = Image.open(r"C:\minproject image\Screenshot 2024-12-07 225820.png")
        img_middle=img_middle.resize((1530,130))
        self.photoimg_middle=ImageTk.PhotoImage(img_middle)
        # img_middle=Label(self.root,image=self.photoimg_middle)
        f_lbl=Label(self.root,image=self.photoimg_middle)
        f_lbl.place(x=0,y=400,width=1530,height=130)
        
        
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("Arial",25,"italic"),bg="lightpink",fg="black")
        b1_1.place(x=650,y=425,width=280,height=70)
        
        img_bottom = Image.open(r"C:\minproject image\WhatsApp Image 2024-12-07 at 22.53.30_3c9401dd.jpg")
        img_bottom=img_bottom.resize((1530,355))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=530,width=1530,height=355)
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # gray scale image

            imageNp=np.array(img,'uint8') #datatype
            id=int(os.path.split(image)[1].split('.')[1])

            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training ",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
    

    #========= Train the classifier and save====
        clf=cv2.face.LBPHFaceRecognizer_create()  # Local Binary pattern use to train a data
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed !!")
        
if __name__ == "__main__":
  root=Tk()
  obj=Train(root)
  root.mainloop()