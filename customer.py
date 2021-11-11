from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk

class Cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("'Parking Management System")
        self.root.geometry("1295x550+230+220")

# **************title*************
        lbl_title=Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
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

        enty_ref=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        enty_ref.grid(row=0,column=1)

#cust name
        cname=Label(labelframeleft,text="Customer Name:",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtcname.grid(row=1,column=1)

# mother name
        mname=Label(labelframeleft,text="Mother Name:",font=("arial",12,"bold"),padx=2,pady=6)
        mname.grid(row=2,column=0,sticky=W)

        txtmname=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtmname.grid(row=2,column=1)

# gender combobox
        label_gender=Label(labelframeleft,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

# Vehicle number
        lbl_vehicle=Label(labelframeleft,text="Vehicle Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_vehicle.grid(row=4,column=0,sticky=W)

        txtvehicle=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtvehicle.grid(row=4,column=1)

# mobile number
        label_mobile=Label(labelframeleft,text="Mobile Number:",font=("arial",12,"bold"),padx=2,pady=6)
        label_mobile.grid(row=5,column=0,sticky=W)

        txtmobile=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtmobile.grid(row=5,column=1)

 # email
        label_email=Label(labelframeleft,text="Email:",font=("arial",12,"bold"),padx=2,pady=6)
        label_email.grid(row=6,column=0,sticky=W)

        txtemail=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtemail.grid(row=6,column=1)

# nationality
        label_nation=Label(labelframeleft,text="Nationality:",font=("arial",12,"bold"),padx=2,pady=6)
        label_nation.grid(row=7,column=0,sticky=W)

        combo_nation=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
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

        txtid=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtid.grid(row=9,column=1)
# address
        label_address=Label(labelframeleft,text="Address:",font=("arial",12,"bold"),padx=2,pady=6)
        label_address.grid(row=10,column=0,sticky=W)

        txtaddress=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtaddress.grid(row=10,column=1)

# ***************buttons****************
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

 # *****************table frame*****************

        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
        Table_frame.place(x=435,y=50,width=860,height=490)    

        lbl_searchby=Label(Table_frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lbl_searchby.grid(row=0,column=0,sticky=W,padx=2)

        combo_search=ttk.Combobox(Table_frame,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Mobile","Ref No.")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        txtsearch=ttk.Entry(Table_frame,width=24,font=("arial",13,"bold"))
        txtsearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_frame,text="Search",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_frame,text="Show All",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

# ***************show data table*****************

        details_frame=Frame(Table_frame,bd=2,relief=RIDGE)
        details_frame.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_frame,column=("ref","name","mother","gender","vehicle no.","mobile","email","nationality",
        "idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
         
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Ref Number")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("vehicle no.",text="Vehicle Number")
        self.Cust_Details_Table.heading("mobile",text="Mobile Number")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="ID Proof")
        self.Cust_Details_Table.heading("idnumber",text="ID Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)



        
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("vehicle no.",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)




        



if __name__ == "__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()