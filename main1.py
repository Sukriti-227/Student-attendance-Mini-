from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from developer import Developer
from face_recognition import Face_recognition
from help import Help
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Face Recognition System")
        
        #First Image
        img=Image.open(r"C:\minproject image\Screenshot 2024-12-05 202307.png")
        img=img.resize((510,200))
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0)
        
        #Second Image
        img2=Image.open(r"C:\minproject image\Screenshot 2024-12-05 201854.png")
        img2=img2.resize((510,200))
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=510,y=0)
        
        #Third Image
        img3=Image.open(r"C:\minproject image\Screenshot 2024-12-05 202117.png")
        img3=img3.resize((510,200))
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1020,y=0)
        
        #Background image
        img4=Image.open(r"C:\minproject image\gh.jpg")
        img4=img4.resize((1530,710))
        self.photoimg4=ImageTk.PhotoImage(img4)
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=200)
        
        #title button
        title_lbl=Label(bg_img,text="STUDENT  FACE  RECOGNITION  ATTENDANCE  SYSTEM",font=("Times New Roman",30,"italic","bold"),fg="blue",bg="white")
        title_lbl.place(x=0,y=0,width=1530,height=40)
        
        #student button
        img5=Image.open(r"C:\minproject image\stu1.jpg")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Arial",15,"italic"),bg="lightpink",fg="black")
        b1_1.place(x=200,y=300,width=220,height=40)
        
         #face detection button
        img6=Image.open(r"C:\minproject image\Screenshot 2024-12-05 200744.png")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)
        b2=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.Face_recognition)
        b2.place(x=500,y=100,width=220,height=220)
        b2_1=Button(bg_img,text="Face Recognition",cursor="hand2",command=self.Face_recognition,font=("Arial",15,"italic"),bg="lightpink",fg="black")
        b2_1.place(x=500,y=300,width=220,height=40)

        #Attendance button
        img7=Image.open(r"C:\minproject image\WhatsApp Image 2024-12-05 at 00.12.21_a2740402.jpg")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)
        b3=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance)
        b3.place(x=800,y=100,width=220,height=220)
        b3_1=Button(bg_img,text="Attendance",command=self.attendance,cursor="hand2",font=("Arial",15,"italic"),bg="lightpink",fg="black")
        b3_1.place(x=800,y=300,width=220,height=40)

        #Help desk button
        img8=Image.open(r"C:\minproject image\help.jpg")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)
        b4=Button(bg_img,image=self.photoimg8,command=self.help_desk,cursor="hand2")
        b4.place(x=1100,y=100,width=220,height=220)
        b4_1=Button(bg_img,text="Help Desk",command=self.help_desk,cursor="hand2",font=("Arial",15,"italic"),bg="lightpink",fg="black")
        b4_1.place(x=1100,y=300,width=220,height=40)
        
         #Train data button
        img9=Image.open(r"C:\minproject image\stock-vector-tiny-business-characters-with-gears-at-huge-cyborg-head-artificial-intelligence-machine-learning-2137939893.jpg")
        img9=img9.resize((220,220))
        self.photoimg9=ImageTk.PhotoImage(img9)
        b5=Button(bg_img,image=self.photoimg9,command=self.train_data,cursor="hand2")
        b5.place(x=200,y=380,width=220,height=220)
        b5_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("Arial",15,"italic"),bg="lightpink",fg="black")
        b5_1.place(x=200,y=570,width=220,height=40)
        
        #Photos Button
        img11=Image.open(r"C:\minproject image\Screenshot 2024-12-07 190934.png")
        img11=img11.resize((220,220))
        self.photoimg11=ImageTk.PhotoImage(img11)
        b7=Button(bg_img,image=self.photoimg11,command=self.open_img,cursor="hand2")
        b7.place(x=500,y=380,width=220,height=220)
        b7_1=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("Arial",15,"italic"),bg="lightpink",fg="black")
        b7_1.place(x=500,y=570,width=220,height=40)
        
        
        #Developer Button
        img12=Image.open(r"C:\minproject image\Screenshot 2024-12-07 192051.png")
        img12=img12.resize((220,220))
        self.photoimg12=ImageTk.PhotoImage(img12)
        b8=Button(bg_img,command=self.dev_data,image=self.photoimg12,cursor="hand2",)
        b8.place(x=800,y=380,width=220,height=220)
        b8_1=Button(bg_img,command=self.dev_data,text="Developer",cursor="hand2",font=("Arial",15,"italic"),bg="lightpink",fg="black")
        b8_1.place(x=800,y=570,width=220,height=40)
        
        
         #Exit button
        img10=Image.open(r"C:\minproject image\Screenshot 2024-12-05 194150.png")
        img10=img10.resize((220,220))
        self.photoimg10=ImageTk.PhotoImage(img10)
        b6=Button(bg_img,image=self.photoimg10,command=self.iExit,cursor="hand2")
        b6.place(x=1100,y=380,width=220,height=220)
        b6_1=Button(bg_img,text="Exit Button",command=self.iExit,cursor="hand2",font=("Arial",15,"italic"),bg="lightpink",fg="black")
        b6_1.place(x=1100,y=570,width=220,height=40)
    
    def open_img(self):
        os.startfile("data")   
    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project")
        if self.iExit>0:
            self.root.destroy()
        else:
            return
        # FUNCTIONS BUTTONS
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def Face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
    
    def dev_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)  
        
    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)  

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)  
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
    