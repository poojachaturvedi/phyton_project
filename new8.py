from tkinter import*
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import random




class Cust_win:

    def __init__(self,root):
        self.root=root
        self.root.title("'Parking Management System")
        self.root.geometry("1295x550+230+220")


#variable#
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_name=tk.StringVar()
        self.var_mother=tk.StringVar()
        self.var_gender=tk.StringVar()
        self.var_Vno=tk.StringVar()
        self.var_mobile=tk.StringVar()
        self.var_email=tk.StringVar()
        self.var_nationality=tk.StringVar()
        self.var_address=tk.StringVar()
        self.var_id_proof=tk.StringVar()
        self.var_id_number=tk.StringVar()

        

# **************title*************
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS", font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


# *************logo***************     
        img2=Image.open(r"D:\parking_management_system\photo-1543465077-db45d34b88a5.jpg")
        img2=img2.resize((100,50),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=50)

# *************labelFrame*************
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

# ************labels and entrys**********
# custref
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",13,"bold"),state="readonly")
        enty_ref.grid(row=0,column=1)

#custname
        cname=Label(labelframeleft,text="Customer Name:",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_name,width=29,font=("arial",13,"bold"))
        txtcname.grid(row=1,column=1)
#mother
        mname=Label(labelframeleft,text="Mother:",font=("arial",12,"bold"),padx=2,pady=6)
        mname.grid(row=2,column=0,sticky=W)

        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,width=29,font=("arial",13,"bold"))
        txtmname.grid(row=2,column=1)
# gender combobox
        label_gender=Label(labelframeleft,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
# Vehicle number
        lbl_vehicle=Label(labelframeleft,text="Vehicle Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_vehicle.grid(row=4,column=0,sticky=W)

        txtvehicle=ttk.Entry(labelframeleft,textvariable=self.var_Vno,width=29,font=("arial",13,"bold"))
        txtvehicle.grid(row=4,column=1)
# mobile number
        label_mobile=Label(labelframeleft,text="Mobile Number:",font=("arial",12,"bold"),padx=2,pady=6)
        label_mobile.grid(row=5,column=0,sticky=W)

        txtmobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("arial",13,"bold"))
        txtmobile.grid(row=5,column=1)

 # email
        label_email=Label(labelframeleft,text="Email:",font=("arial",12,"bold"),padx=2,pady=6)
        label_email.grid(row=6,column=0,sticky=W)

        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("arial",13,"bold"))
        txtemail.grid(row=6,column=1)

# nationality
        label_nation=Label(labelframeleft,text="Nationality:",font=("arial",12,"bold"),padx=2,pady=6)
        label_nation.grid(row=7,column=0,sticky=W)

        combo_nation=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_nation["value"]=("Indian","American","British")
        combo_nation.current(0)
        combo_nation.grid(row=7,column=1)

        # idproof combobox
        label_idproof=Label(labelframeleft,text="ID Proof:",font=("arial",12,"bold"),padx=2,pady=6)
        label_idproof.grid(row=8,column=0,sticky=W)

        combo_idproof=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_idproof["value"]=("AdharCard","Driving Liscence","Passport")
        combo_idproof.current(0)
        combo_idproof.grid(row=8,column=1)
     
# id number
        label_id=Label(labelframeleft,text="ID Number:",font=("arial",12,"bold"),padx=2,pady=6)
        label_id.grid(row=9,column=0,sticky=W)

        txtid=ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=29,font=("arial",13,"bold"))
        txtid.grid(row=9,column=1)
# address
        label_address=Label(labelframeleft,text="Address:",font=("arial",12,"bold"),padx=2,pady=6)
        label_address.grid(row=10,column=0,sticky=W)

        txtaddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("arial",13,"bold"))
        txtaddress.grid(row=10,column=1)



# ***************buttons****************
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)


# *****************table frame search*****************

        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
        Table_frame.place(x=435,y=50,width=860,height=490)    

        lbl_searchby=Label(Table_frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lbl_searchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()

        combo_search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Mobile","Ref No.")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(Table_frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        txtsearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_frame,text="Search",command=self.search_data,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

# ***************show data table*****************

        details_frame=Frame(Table_frame,bd=2,relief=RIDGE)
        details_frame.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_frame,column=("ref","name","mother","gender","vno","mobile","email","nationality","id_proof","id_number","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
         
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Ref Number")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("vno",text="Vehicle No.")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("id_proof",text="Id_Proof")
        self.Cust_Details_Table.heading("id_number",text="Id_Number")
        self.Cust_Details_Table.heading("address",text="Address")
        
        
        
        

        self.Cust_Details_Table["show"]="headings"
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)



        
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("vno",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("id_proof",width=100)
        self.Cust_Details_Table.column("id_number",width=100)
        self.Cust_Details_Table.column("address",width=100)
        
       
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
    def add_data(self):
        if self.var_name.get()=="" :
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password="Pooja",database="k20ts1")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO cust1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),self.var_name.get(),self.var_mother.get(),self.var_gender.get(),self.var_Vno.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),self.var_id_proof.get(),self.var_id_number.get(),self.var_address.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es1:
                messagebox.showwarning("Warning",f"Somwthing went wrong:{str(es1)}")

       
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password="Pooja",database="k20ts1")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from cust1")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_rows=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_rows)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_Vno.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    def update_data(self):
        if(self.var_mobile.get()==""):
            messagebox.showerror("Error","Please Enter mobile Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password="Pooja",database="k20ts1")
            my_cursor=conn.cursor()
            my_cursor.execute("update cust1 set name=%s,mother=%s,gender=%s,vno=%s,mobile=%s,email=%s,nationality=%s,proof=%s,number=%s,address=%s where ref=%s",
            (self.var_name.get(),self.var_mother.get(),self.var_gender.get(),self.var_Vno.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),self.var_id_proof.get(),self.var_id_number.get(),self.var_address.get(),self.var_ref.get())
            )
                                                                                                                    
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Details has been updated Successfully.",parent=self.root)

    def delete_data(self):
        delete_data=messagebox.askyesno("Parking Management System","Do you want to delete this customer?",parent=self.root)
        if delete_data>0:
            conn=mysql.connector.connect(host='localhost',username='root',password="Pooja",database="k20ts1")
            my_cursor=conn.cursor()
            query="delete from cust1 where ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
                if not delete_data:
                    return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset_data(self):
        
        
        #self.var_ref.set(""),
        self.var_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_Vno.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


    def search_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password="Pooja",database="k20ts1")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from cust1 where "+str(self.search_var.get())+" LIKE '% "+str(self.txt_search.get())+"%' ")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()