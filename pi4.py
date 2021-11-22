#parking management system
from tkinter import*
from PIL import Image, ImageTk
from new4 import Area_Booking
from new8 import Cust_win
from DETAILS import Area




class ParkingManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("'Parking Management System")
        self.root.geometry("1550x800+0+0")
# ************* 1st Img ****************
        img1=Image.open(r"D:\parking_management_system\photo-1543465077-db45d34b88a5.jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
# ************* Logo *****************
        img2=Image.open(r"D:\parking_management_system\photo-1506521781263-d8422e82f27a.jpg")
        img2=img2.resize((3550,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)
# *************title****************
        lbl_title=Label(self.root, text="Parking Management System", font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
# *********** in frame***************
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

# **********menu******************
        lbl_menu=Label(main_frame, text="MENU", font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

# ********button***********
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        platform_btn=Button(btn_frame,text="PLATFORM",command=self.area_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        platform_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",width=22,command=self.all_details,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

       
        logout_btn=Button(btn_frame,text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

        img3=Image.open(r"D:\parking_management_system\photo-1553203911-ba17267172da.jpg")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)

# **************down image***********
        
        img4=Image.open(r"D:\parking_management_system\photo-1578859695220-856a4f5edd39.jpg")
        img4=img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1=Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0,y=225,width=230,height=210)

        
        img5=Image.open(r"D:\parking_management_system\photo-1573348722427-f1d6819fdf98.jpg")
        img5=img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0,y=420,width=230,height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)

    def area_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Area_Booking(self.new_window)
   
    def all_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Area(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj=ParkingManagementSystem(root)
    root.mainloop()
