from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Area_Details:
    def __init__(self,root):
        self.root=root
        self.root.title("Room Details")
        self.root.geometry("1295x550+80+175")

# **************title*************
        lbl_title=Label(self.root, text=" DETAILS", font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

# *************logo***************     
        img2=Image.open(r"D:\parking_management_system\photo-1543465077-db45d34b88a5.jpg")
        img2=img2.resize((100,50),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=50)

# *************labelFrame*************
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Area Side",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)

#platform area 
        cname=Label(labelframeleft,text="Platform Area",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtcname.grid(row=1,column=1)

# area type 
        aty=Label(labelframeleft,text="Area Type",font=("arial",12,"bold"),padx=2,pady=6)
        aty.grid(row=2,column=0,sticky=W)

        txtaty=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtaty.grid(row=2,column=1)
#Area Number
        ano=Label(labelframeleft,text="Area Number",font=("arial",12,"bold"),padx=2,pady=6)
        ano.grid(row=3,column=0,sticky=W)

        txtano=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtano.grid(row=3,column=1)
#btn frame and buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=400,height=40)

        btnAdd=Button(btn_frame,text="Add",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=4,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=4,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=4,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=4,column=3,padx=1)



if __name__ == "__main__":
    root=Tk()
    obj=Area_Details(root)
    root.mainloop()
