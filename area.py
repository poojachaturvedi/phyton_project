#area details 
from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Area_Booking:
    def __init__(self,root):
        self.root=root
        self.root.title("'Parking Management System")
        self.root.geometry("1295x550+80+175")

#variables
        self.var_contact=StringVar()
        self.var_Parking_Date=StringVar()
        self.var_Removal_Date=StringVar()
        self.var_Area_Type=StringVar()
        self.var_Available_Area=StringVar()
        self.var_Number_of_days=StringVar()
        self.var_subtotal=StringVar()
        self.var_Totalcost=StringVar()

# **************title*************
        lbl_title=Label(self.root, text="AREA BOOKING  DETAILS", font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

# *************logo***************     
        img2=Image.open(r"D:\parking_management_system\photo-1543465077-db45d34b88a5.jpg")
        img2=img2.resize((100,50),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=50)

    # *************labelFrame*************
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Area Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

    # ************labels and entrys**********
# custcontact
        lbl_cust_contact=Label(labelframeleft,textvariable=self.var_contact,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        enty_contact=ttk.Entry(labelframeleft,width=20,font=("arial",13,"bold"))
        enty_contact.grid(row=0,column=1,sticky=W)

#fetch data button
        btnfetchdata=Button(labelframeleft,text="Fetch data",width=8,font=("arial",8,"bold"),bg="black",fg="yellow")
        btnfetchdata.place(x=347,y=4)
    
#parking_date
        check_in_date=Label(labelframeleft,textvariable=self.var_Parking_Date,text="Parking Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1)

# removal_date
        check_out_date=Label(labelframeleft,textvariable=self.var_Removal_Date,text="Removal Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)

        txtcheck_out_date=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtcheck_out_date.grid(row=2,column=1)
        
# area type combobox
        label_area_type=Label(labelframeleft,textvariable=self.var_Area_Type,text="Area Type:",font=("arial",12,"bold"),padx=2,pady=6)
        label_area_type.grid(row=3,column=0,sticky=W)
        combo_area_type=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_area_type["value"]=("Car","Cycle","bike","Other")
        combo_area_type.current(0)
        combo_area_type.grid(row=3,column=1)

# available area 
        lbl_area_Available=Label(labelframeleft,textvariable=self.var_Available_Area,text="Available Area:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_area_Available.grid(row=4,column=0,sticky=W)

        txtareaavailable=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtareaavailable.grid(row=4,column=1)

# NUmber of days
        label_nod=Label(labelframeleft,textvariable=self.var_Number_of_days,text="Number of Days:",font=("arial",12,"bold"),padx=2,pady=6)
        label_nod.grid(row=5,column=0,sticky=W)

        txtnod=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtnod.grid(row=5,column=1)

 # paid tax
        label_tax=Label(labelframeleft,text="Email:",font=("arial",12,"bold"),padx=2,pady=6)
        label_tax.grid(row=6,column=0,sticky=W)

        txttax=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txttax.grid(row=6,column=1)

# sub total
        label_st=Label(labelframeleft,textvariable=self.var_subtotal,text="Subtotal:",font=("arial",12,"bold"),padx=2,pady=6)
        label_st.grid(row=7,column=0,sticky=W)

        txtst=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtst.grid(row=7,column=1)
# Total Cost
        label_tc=Label(labelframeleft,textvariable=self.var_Totalcost,text="TotalCost",font=("arial",12,"bold"),padx=2,pady=6)
        label_tc.grid(row=8,column=0,sticky=W)

        txttc=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txttc.grid(row=8,column=1,padx=1,sticky=W)

#bill button
        btnbill=Button(labelframeleft,text="Bill",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnbill.grid(row=10,column=0,padx=1,sticky=W)
        
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

#right side image
        img3=Image.open(r"D:\parking_management_system\photo-1573348722427-f1d6819fdf98.jpg") 
        img3=img3.resize((500,300),Image.ANTIALIAS) 
        self.photoimg3=ImageTk.PhotoImage(img3)   
        lbling=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lbling.place(x=760,y=55,width=500,height=300)   

# *****************frame search system*****************

        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
        Table_frame.place(x=435,y=280,width=860,height=260)  

        self.search_var=StringVar()


        lbl_searchby=Label(Table_frame,textvariable=self.search_var,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lbl_searchby.grid(row=0,column=0,sticky=W,padx=2)

        combo_search=ttk.Combobox(Table_frame,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Contact","Area")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)


        self.txt_search=StringVar()
        txtsearch=ttk.Entry(Table_frame,width=24,font=("arial",13,"bold"))
        txtsearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_frame,text="Search",textvariable=self.txt_search,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_frame,text="Show All",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

# ***************show data table*****************

        details_frame=Frame(Table_frame,bd=2,relief=RIDGE)
        details_frame.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL)

        self.Area_Table=ttk.Treeview(details_frame,column=("Contact","ParkingDate","Removaldate","Areatype","Available_area","Numberofdays","Subtotal","Totalcost"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
   
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        #scroll_x.config(command=self.Area_Table.xview)
        #scroll_y.config(command=self.Area_Table.yview)

        self.Area_Table.heading("Contact",text="Contact")
        self.Area_Table.heading("ParkingDate",text="Parking_Date")
        self.Area_Table.heading("RemovalDate",text="Removal_Date")
        self.Area_Table.heading("AreaType",text="Area_Type")
        self.Area_Table.heading("Available_Area",text="Available_Area")
        self.Area_Table.heading("Number_of_days",text="Number_Of_Days")
        self.Area_Table.heading("subtotal",text="SubTotal")
        self.Area_Table.heading("Totalcost",text="TotalCost")
        

       ''' self.Area_Table["show"]="headings"
        self.Area_Table.pack(fill=BOTH,expand=1)'''

#all data fetch
'''def fetch_contact(self):
        if self.var_contact.get()=="":
                messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
                 conn=mysql.connector.connect(host="localhost",username="root",password="Pooja",database="parking_management_system")
                 my_cursor=conn.cursor()
                 query=("select * from customer where mobile=%s")
                 value=(self.var_contact.get(),)
                 my_cursor.execute(query,value)
                 row=my_cursor.fetchone()

                 if row==None:
                         messagebox.showerror("Error","This Number Not found",parent=self.root)
                 else:

                 conn.commit()
                 conn.close()

                 showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                 showDataframe.place(x=450,y=55,width=300,height=180)

                 lblName=Label(showDataframe,text="Name:",font=("Arial",12,"bold"))
                 lblName.place(x=0,y=0)

                 lbl=Label(showDataframe,text=row,font=("Arial",12,"bold"))
                 lbl.place(x=90,y=0)

                 conn=mysql.connector.connect(host="localhost",username="root",password="Pooja",database="parking_management_system")
                 my_cursor=conn.cursor()
                 query=("select Gender from customer where mobile=%s")
                 value=(self.var_contact.get(),)
                 my_cursor.execute(query,value)
                 row=my_cursor.fetchone()

                 lblGender=Label(showDataframe,text="Gender:",font=("Arial",12,"bold"))
                 lblGender.place(x=0,y=30)

                 lb2=Label(showDataframe,text=row,font=("Arial",12,"bold"))
                 lb2.place(x=90,y=30)

def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
                messagebox.showerror("Error","All fields are required")
        else:
                try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Pooja",database="parking_management_system")
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_contact.get(),
                                                                                        self.var_Parking_Date.get(),
                                                                                        self.var_Removal_Date.get(),
                                                                                        self.var_Area_Type.get(),
                                                                                        self.var_Available_Area.get(),
                                                                                        self.var_Number_of_days.get(),
                                                                                        self.var_subtotal.get(),
                                                                                        self.var_Totalcost.get()
                                                                
                                                                                        ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()                                                                
                        messagebox.showinfo("Success","Customer has been added")
                except Exception as es:
                        messagebox.showwarning("Warning","Something went wrong:{str(es)}",parent=self.root)
       
def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Pooja",database="parking_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from area")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.area.delete(*self.area_.get_children())
                for i in rows:
                        self.area.insert("",END,values=i)
                conn.commit
        conn.close

def get_cursor(self,event=""):
        cursor_row=self.Area_Table.focus()
        cursor=self.Area_Table.item(cursor_row)
        row=content["values"]

        self.var_Contact.set(row[0])
        self.var_Parking_Date.set(row[1])
        self.var_Removal_Date.set(row[2])
        self.var_Number_of_days.set(row[3])
        self.var_Area_Type.set(row[4])
        self.var_Area_Available.set(row[5])
        self.var_Subtotal.set(row[6])
        self.var_Totalcost.set(row[7])
       
def update(self):
        if self.var_mobile.get()=="":
                messagebox.showerror("Error","Please Enter mobile number",parent=self.root)
        else:
                conn=mysql.connector(host="localhost",username="root",password="Pooja",database="parking_management_system")
                my_cursor=conn.cursor()
                my_cursor.execute("Update customer set NAME=%s,MOTHER=%s,GENDER=%s,VEHICLENUMBER=%s,MOBILE=%s,EMAIL=%s,NATIONALITY=%s,IDPROOF=%s,IDNUMBER=%s,ADDRESS=%s  where REF=%s",
                                                                                                                                                                                (
                                                                                        self.var_contact.get(),
                                                                                        self.var_Parking_Date.get(),
                                                                                        self.var_Removal_Date.get(),
                                                                                        self.var_Area_Type.get(),
                                                                                        self.var_Available_Area.get(),
                                                                                        self.var_Number_of_days.get(),
                                                                                        self.var_subtotal.get(),
                                                                                        self.var_Totalcost.get()                                                                                                                                                                                     
                                                                                                                                                                                       
                                                                                                                                                                ))

                conn.commit()
                conn.close()
                messagebox.showinfo("Update","Customer details have been executed successfully",paremy=self.root)

def Delete_Data(self):
        Delete_Data=messagebox.askyesno("Parking Management System","Do you want to delete  this customer",parent=self.root)
        if Delete_Data>0:
                conn=mysql.connector.connect(host="localhost",username="root",password="Pooja",database="management")
                my_cursor=conn.cursor()
                query="delete from customer REF=%s"
                values=(self.var_ref.get(),)
                my_cursor.execute(query,value)
        else:
                if not Delete_Data:
                        return
        conn.commit()
        self.fetchdata()
        conn.close()

def Reset_data(self):
        self.var_ref.set("") 
        self.var_name.set("")
        self.mother.set("")                                                                                                                                                                            
        self.var_vno.set(""),                                                                                                                                                                         
        self.var_mobile.set(""),                                                                                                                                                            
        self.var_email.set(""),                                                                                                                                                                                                                                             
        self.var_id_number.set(""),                                                                                                                                                          
        self.var_address.set("")                                                                                                                                                                        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x)) 
'''
if __name__ == "__main__":
    root=Tk()
    obj=Area_Booking(root)
    root.mainloop()