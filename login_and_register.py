from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox  
import mysql.connector

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()


class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1550x800+0+0")
        self.bg=ImageTk.PhotoImage(file=r"D:\parking_management_system\photo-1543465077-db45d34b88a5.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=170,width=340,height=450)
        
        img1=Image.open(r"D:\parking_management_system\icon.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        #antilias-->converts high level to low lwvel
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        #borderwidth-->reduces extra border
        lblimg1.place(x=615,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        ###icon images##
        img2=Image.open(r"D:\parking_management_system\icon.jpg")
        img2=img1.resize((25,25),Image.ANTIALIAS)
        #antilias-->converts high level to low lwvel
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        #borderwidth-->reduces extra border
        lblimg2.place(x=540,y=323,width=25,height=25)

        img3=Image.open(r"D:\parking_management_system\lockimage1.jpg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        #antilias-->converts high level to low lwvel
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        #borderwidth-->reduces extra border
        lblimg3.place(x=540,y=397,width=25,height=25)

        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="White",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="White",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=3,y=350,width=160)

        forwardbtn=Button(frame,text="Forgot Password",font=("times new roman",10,"bold"),borderwidth=0,fg="White",bg="black",activeforeground="white",activebackground="black")
        forwardbtn.place(x=15,y=370,width=120,height=35)

    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
            
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required")
        elif self.txtuser.get()=="Kapu" and self.txtpass.get()=="ashu":
            messagebox.show("success","wELCOME TO PS parking ")
        else:
             messagebox.showerror("Error","All fields required")

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        self.root.configure(bg="sky blue")
        #self.bg=ImageTk.PhotoImage(file=r"D:\parking_management_system\photo-1553203911-ba17267172da.jpg")
        #bg_lbl=Label(self.root,image=self.bg)
        #bg_lbl.place(x=0,y=0,relheight=1,relwidth=1)

        ####variables###
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        ####backfround image####
        self.bg1=ImageTk.PhotoImage(file=r"D:\parking_management_system\photo-1543465077-db45d34b88a5.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=70,y=100,height=550,width=470)
        
        ####frame and register label#####
        frame=Frame(self.root,bg="white")
        frame.place(x=545,y=100,height=550,width=800)
         
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #######labels and entries#######

        #fname label and entry#
        fname=Label(frame,text="First Name",font=("times new roman",20,"bold"),bg="white")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",20,"bold"))
        fname_entry.place(x=50,y=130,width=220)

        #lname label and entry#
        lname=Label(frame,text="Last Name",font=("times new roman",20,"bold"),bg="white")
        lname.place(x=370,y=100)
        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",20,"bold"))
        lname_entry.place(x=370,y=130,width=220)

        #contact label and entry#
        contact=Label(frame,text="Contact No",font=("times new roman",20,"bold"),bg="white")
        contact.place(x=50,y=170)
        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",20,"bold"))
        contact_entry.place(x=50,y=200,width=220)

        ##email label and entry##
        email=Label(frame,text="Email",font=("times new roman",20,"bold"),bg="white")
        email.place(x=370,y=170)
        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",20,"bold"))
        email_entry.place(x=370,y=200,width=220)

        #security question label and entry###
        security_Q=Label(frame,text="Select Security Question,",font=("times new roman",20,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman ",20,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Biirth Place","Your school name","Your college name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        #security answer label and entry#
        security_A=Label(frame,text="Security Answer",font=("times new roman",20,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)
        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",20,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        #password label and entry#
        pswd=Label(frame,text="Password",font=("times new roman",20,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        #confirm password label and entry#
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",20,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        ###check button###
        self.var_check=IntVar()
        check_btn=Checkbutton(frame,variable=self.var_check,text="I agree the terms and conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        check_btn.place(x=50,y=370)


        #####################buttons###################

        ##register now button##
        img=Image.open(r"D:\parking_management_system\register_now.jpg")
        img=img.resize((250,70),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,command=self.register_data,image=self.photoimage,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=470,width=300)

        ###login now button###
        img1=Image.open(r"D:\parking_management_system\login_now.jpg")
        img1=img1.resize((250,70),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b2.place(x=350,y=470,width=300)
#function declaration###

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ=="Select"  :
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Pooja",database="parking_management_system")
            my_cursor=conn.cursor()
            query=("select * from register where email= %s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists,pLease enter another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_fname.get(),
                                                                                            self.var_lname.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_securityQ().get(),
                                                                                            self.var_SecurityA().get(),
                                                                                            self.var_pass.get(),
                                                                                            self.var_contact.get
                                                                                        ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successful")

if __name__=="__main__":
    main()