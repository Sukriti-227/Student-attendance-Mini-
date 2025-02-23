from tkinter import*    # it is use for making GUI interface
from tkinter import ttk     #it is use for styleing
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

# making a student class
class Help:
  # making a constructor
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Face Recognition System")
        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",30,"bold"),bg="lightgrey",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top = Image.open(r"C:\minproject image\Screenshot 2024-12-08 161529.png")
        img_top=img_top.resize((1530,850))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1530,height=850)  
        
        dev_label=Label(f_lbl,text="CONTACT US: ",font=("times new roman",25,"bold"),bg="lightgrey",fg="black")
        dev_label.place(x=975,y=600)
        dev_label1=Label(f_lbl,text="sukgang.3007@gmail.com",font=("times new roman",15,"bold"),fg="darkgreen")
        dev_label1.place(x=1200,y=645)
          
if __name__ == "__main__":
  root=Tk()
  obj=Help(root)
  root.mainloop()