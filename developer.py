from tkinter import*    # it is use for making GUI interface
from tkinter import ttk     #it is use for styleing
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

# making a student class
class Developer:
  # making a constructor
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",30,"bold"),bg="lightgreen",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top = Image.open(r"C:\minproject image\Screenshot 2024-12-07 200259.png")
        img_top=img_top.resize((1530,850))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1530,height=850)
        
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=40,width=500,height=720)
        
        img_top1 = Image.open(r"C:\minproject image\IMG_20230203_231025_801 n.jpg")
        img_top1= img_top1.resize((250,250))
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
        f_lbl1=Label(main_frame,image=self.photoimg_top1)
        f_lbl1.place(x=280,y=10,width=220,height=220)
        
        #DEveloper info
        dev_label=Label(main_frame,text="Hello ! My name is Sukriti",font=("times new roman",15,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=5)
        
        img_top2 = Image.open(r"C:\minproject image\IMG-20240602-WA0040.jpg")
        img_top2= img_top2.resize((200,200))
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)
        
        f_lbl2=Label(main_frame,image=self.photoimg_top2)
        f_lbl2.place(x=280,y=250,width=200,height=200)
        
        dev_label=Label(main_frame,text="Hello ! My name is Vishakha",font=("times new roman",15,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=250)
        
        
        img_top3 = Image.open(r"C:\minproject image\WhatsApp Image 2024-12-08 at 01.43.38_e570183e.jpg")
        img_top3= img_top3.resize((200,200))
        self.photoimg_top3=ImageTk.PhotoImage(img_top3)
        
        f_lbl3=Label(main_frame,image=self.photoimg_top3)
        f_lbl3.place(x=280,y=500,width=200,height=200)
        
        dev_label=Label(main_frame,text="Hello ! My name is Sneha",font=("times new roman",15,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=500)

        
if __name__ == "__main__":
  root=Tk()
  obj=Developer(root)
  root.mainloop()