from tkinter import *
from tkinter import ttk
import pymysql
import tkinter.messagebox
from tkinter import messagebox

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1400x750+0+0")

        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="#f3ca20", fg="black")
        title.pack(side=TOP, fill=X)

        # all variable
        self.Batch_var = StringVar()
        self.Department_var = StringVar()
        self.Year_var = StringVar()
        self.PRN_No_var = StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        self.DOB_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()


        # Manage Frame
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#f3ca20")
        Manage_Frame.place(x=40, y=100, width=550, height=550)

        m_title = Label(Manage_Frame, text="Manage Students", bg="#f3ca20", fg="black",
                        font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=10)

         
        lbl_Batch = Label(Manage_Frame, text="Batch", bg="#f3ca20", fg="black", font=("times new roman", 15, "bold"))
        lbl_Batch.grid(row=1, column=0, pady=5, padx=20, sticky="w")

        combo_Batch = ttk.Combobox(Manage_Frame,textvariable=self.Batch_var, font=("times new roman", 13, "bold"), state='readonly',justify=CENTER)
        combo_Batch['values'] = ("Select","2015-16", "2016-17", "2017-18","2018-19","2019-20","2020-21")
        combo_Batch.grid(row=1, column=1, padx=20, pady=5)
        combo_Batch.current(0)    
        
        lbl_Department = Label(Manage_Frame, text="Department", bg="#f3ca20", fg="black", font=("times new roman", 15, "bold"))
        lbl_Department.grid(row=2, column=0, pady=5, padx=20, sticky="w")

        combo_Department = ttk.Combobox(Manage_Frame,textvariable=self.Department_var, font=("times new roman", 13, "bold"), state='readonly',justify=CENTER)
        combo_Department['values'] = ("Select","Computer", "Information Technology", "Electronic and Telecommunication","Electrical","Mechnical","Chemical")
        combo_Department.grid(row=2, column=1, padx=20, pady=5)
        combo_Department.current(0)

        
        lbl_Year = Label(Manage_Frame, text="Year", bg="#f3ca20", fg="black", font=("times new roman", 15, "bold"))
        lbl_Year.grid(row=3, column=0, pady=5, padx=20, sticky="w")

        combo_Year = ttk.Combobox(Manage_Frame,textvariable=self.Year_var, font=("times new roman", 13, "bold"), state='readonly',justify=CENTER)
        combo_Year['values'] = ("Select","F.E", "S.E", "T.E","B.E")
        combo_Year.grid(row=3, column=1, padx=20, pady=5)
        combo_Year.current(0)
        
        lbl_PRN_No = Label(Manage_Frame, text="PRN NO.", bg="#f3ca20", fg="black", font=("times new roman", 15, "bold"))
        lbl_PRN_No.grid(row=4, column=0, pady=5, padx=20, sticky="w")

        txt_PRN_No = Entry(Manage_Frame,textvariable=self.PRN_No_var,font=("times new roman", 12, "bold"), bd=5,relief=GROOVE)
        txt_PRN_No.grid(row=4, column=1, pady=5, padx=20, sticky="w")

    
        lbl_Name = Label(Manage_Frame, text="Name", bg="#f3ca20", fg="black", font=("times new roman", 15, "bold"))
        lbl_Name.grid(row=5, column=0, pady=5, padx=20, sticky="w")

        txt_Name = Entry(Manage_Frame,textvariable=self.Name_var,font=("times new roman", 14, "bold"), bd=5,
                         relief=GROOVE)
        txt_Name.grid(row=5, column=1, pady=5, padx=20, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email", bg="#f3ca20", fg="black", font=("times new roman", 15, "bold"))
        lbl_Email.grid(row=6, column=0, pady=5, padx=20, sticky="w")

        txt_Email = Entry(Manage_Frame,textvariable=self.Email_var,font=("times new roman", 14, "bold"), bd=5,
                          relief=GROOVE)
        txt_Email.grid(row=6, column=1, pady=5, padx=20, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender", bg="#f3ca20", fg="black", font=("times new roman", 15, "bold"))
        lbl_Gender.grid(row=7, column=0, pady=5, padx=20, sticky="w")

        combo_Gender = ttk.Combobox(Manage_Frame,textvariable=self.Gender_var,font=("times new roman", 13, "bold"),state='readonly',justify=CENTER)
        combo_Gender['values'] = ("Select","Male", "Female", "Other")
        combo_Gender.grid(row=7, column=1, padx=20, pady=5)
        combo_Gender.current(0)
        
        lbl_Contact = Label(Manage_Frame, text="Contact", bg="#f3ca20", fg="black",font=("times new roman", 15, "bold"))
        lbl_Contact.grid(row=8, column=0, pady=5, padx=20, sticky="w")

        txt_Contact = Entry(Manage_Frame,textvariable=self.Contact_var,font=("times new roman", 12, "bold"), bd=5,relief=GROOVE)
        txt_Contact.grid(row=8, column=1, pady=5, padx=20, sticky="w")

        lbl_DOB = Label(Manage_Frame, text="D.O.B(dd/mm/yy)", bg="#f3ca20", fg="black", font=("times new roman", 15, "bold"))
        lbl_DOB.grid(row=9, column=0, pady=5, padx=20, sticky="w")

        txt_DOB = Entry(Manage_Frame,textvariable=self.DOB_var,font=("times new roman", 12, "bold"), bd=5,
                         relief=GROOVE)
        txt_DOB.grid(row=9, column=1, pady=5, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address", bg="#f3ca20", fg="black",font=("times new roman", 15, "bold"))
        lbl_Address.grid(row=10, column=0, pady=5, padx=20, sticky="w")

        self.txt_Address = Text(Manage_Frame, width=20, height=4, font=("", 12,"bold"))
        self.txt_Address.grid(row=10, column=1, pady=5, padx=20, sticky="w")

        # button frame
        btn_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#f3ca20")
        btn_Frame.place(x=40, y=650, width=1360,height=70)

        Addbtn = Button(btn_Frame, text="Add", width=20,height=2, command=self.add_students,font=("",10,"bold")).grid(row=0, column=0, padx=20,pady=6)
        Updatebtn = Button(btn_Frame, text="Update", width=20,height=2,command=self.update_data,font=("",10,"bold")).grid(row=0, column=1, padx=10, pady=6)
        deletebtn = Button(btn_Frame, text="Delete", width=20,height=2,command=self.delete_data,font=("",10,"bold")).grid(row=0, column=2, padx=10, pady=6)
        Clearbtn = Button(btn_Frame,text="Clear", width=20,height=2,command=self.clear,font=("",10,"bold")).grid(row=0, column=3, padx=10, pady=6)
        academicabtn = Button(btn_Frame, text="Enter Student marks",width=20,height=2,command=self.academic,font=("",10,"bold")).grid(row=0, column=4, padx=10, pady=6)
        Placemetnbtn = Button(btn_Frame, text="Enter Placement Details",width=20,height=2,command=self.placement,font=("",10,"bold")).grid(row=0, column=5, padx=2, pady=2)
        Logoutbtn = Button(btn_Frame, text="Logout",bg="gray",fg="red",bd=5,command=self.logout,width=18,height=2,font=("",10,"bold")).grid(row=0, column=6, padx=40, pady=6)
        
# detail Frame
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#f3ca20")
        Detail_Frame.place(x=600, y=100, width=800, height=550)

        lbl_search = Label(Detail_Frame, text="Search By", bg="#f3ca20", fg="black",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, width=10,textvariable=self.search_by,font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("PRN_No","Name","Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(Detail_Frame, width=20,textvariable=self.search_txt,font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", width=10, pady=5,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        searchbtn = Button(Detail_Frame, text="ShowAll", width=10, pady=5,command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)
    
        ##table frame
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="black")
        Table_Frame.place(x=10, y=70, width=760, height=450)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame,columns=("Batch","Department","Year","PRN_No", "Name", "Email", "Gender", "Contact", "DOB", "Address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)




        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("Batch",text="Batch")
        self.Student_table.heading("Department",text="Department")
        self.Student_table.heading("Year",text="Year")
        self.Student_table.heading("PRN_No",text="PRN_No")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("Email",text="Email")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Contact",text="Contact")
        self.Student_table.heading("DOB",text="D.O.B")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show'] = 'headings'
        self.Student_table.column("Batch", width=100)
        self.Student_table.column("Department", width=140)
        self.Student_table.column("Year", width=100)      
        self.Student_table.column("PRN_No", width=100)
        self.Student_table.column("Name", width=100)
        self.Student_table.column("Email", width=100)
        self.Student_table.column("Gender", width=100)
        self.Student_table.column("Contact", width=100)
        self.Student_table.column("DOB", width=100)
        self.Student_table.column("Address", width=150)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()

    def add_students(self):
        if  self.PRN_No_var.get()=="" or self.Name_var.get()=="":
            messagebox.showerror("Error","All Fields are required")
        elif self.Batch_var.get()=="" or self.Department_var.get()=="":
            messagebox.showerror("Error","All Fields are required")   
        elif self.Contact_var.get()=="" or self.Email_var.get()=="":
            messagebox.showerror("Error","All Fields are required") 
        elif self.Year_var.get()=="" or self.DOB_var.get()=="":
            messagebox.showerror("Error","All Fields are required")   
          
        elif self.Gender_var.get()=="":
            messagebox.showerror("Error","All Fields are required")   
        
        elif len(self.Contact_var.get())!=10:

                messagebox.showerror("error","please enter correct number")       
        elif len(self.DOB_var.get())!=10:    
                messagebox.showerror("error","please enter correct date") 
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="students")
            cur = con.cursor()
            cur.execute("insert into std value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Batch_var.get(),
                                                                                self.Department_var.get(),
                                                                                self.Year_var.get(),
                                                                                self.PRN_No_var.get(),
                                                                                self.Name_var.get(),
                                                                                self.Email_var.get(),
                                                                                self.Gender_var.get(),
                                                                                self.Contact_var.get(),
                                                                                self.DOB_var.get(),
                                                                                self.txt_Address.get('1.0', END)
                                                                                ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")

    
    
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="students")
        cur=con.cursor()
        cur.execute("select * from std")
        rows=cur.fetchall()
        self.Student_table.delete(*self.Student_table.get_children())
        if len(rows)!=0:
                for row in rows:
                        self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()
            
   
    def clear(self):
            self.Batch_var.set("")
            self.Department_var.set("")
            self.Year_var.set("")
            self.PRN_No_var.set("")
            self.Name_var.set("")
            self.Email_var.set("")
            self.Gender_var.set("")
            self.Contact_var.set("")
            self.DOB_var.set("")
            self.txt_Address.delete("1.0",END)
        
    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        content=self.Student_table.item(cursor_row)
        row=content['values']
        self.Batch_var.set(row[0])
        self.Department_var.set(row[1])
        self.Year_var.set(row[2])
        self.PRN_No_var.set(row[3])
        self.Name_var.set(row[4])
        self.Email_var.set(row[5])
        self.Gender_var.set(row[6])
        self.Contact_var.set(row[7])
        self.DOB_var.set(row[8])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[9])


    def update_data(self):    
        self.Batch_var.get()
        self.Department_var.get()
        self.Year_var.get()
        self.PRN_No_var.get()
        self.Name_var.get()
        self.Email_var.get()
        self.Gender_var.get()
        self.Contact_var.get()
        self.DOB_var.get()
        self.txt_Address.get('1.0', END)
        if self.PRN_No_var.get()=="" or self.Name_var.get()=="":
            messagebox.showerror("Error","Select the record")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="students")
            cur = con.cursor()
            cur.execute("update std set Batch=%s,Department=%s,Year=%s,Name=%s,Email=%s,Gender=%s,Contact=%s,DOB=%s,Address=%s Where PRN_No=%s",(
                                                                            self.Batch_var.get(),
                                                                            self.Department_var.get(),
                                                                            self.Year_var.get(),
                                                                            self.Name_var.get(),
                                                                            self.Email_var.get(),
                                                                            self.Gender_var.get(),
                                                                            self.Contact_var.get(),
                                                                            self.DOB_var.get(),
                                                                            self.txt_Address.get('1.0', END),
                                                                            self.PRN_No_var.get()
                                                                            ))
        con.commit()
        messagebox.showinfo("Success","Record has updated Successfully")                
        
        
        self.fetch_data()
        self.clear()
        con.close()
    
   
    def delete_data(self):
        self.Batch_var.get()
        self.Department_var.get()
        self.Year_var.get()
        self.PRN_No_var.get()
        self.Name_var.get()
        self.Email_var.get()
        self.Gender_var.get()
        self.Contact_var.get()
        self.DOB_var.get()
        self.txt_Address.get('1.0', END)
        if self.PRN_No_var.get()=="" or self.Name_var.get()=="":
            messagebox.showerror("Error","Select the record")
        
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="students")
            cur=con.cursor()
            delete = tkinter.messagebox.askyesno("Delete","Do you want to Delete the record")
            if delete > 0:
                cur.execute("delete from std Where PRN_No=%s",self.PRN_No_var.get())
                
                messagebox.showinfo("Success","Record has deleted Successfully")
                self.clear()
        
            con.commit()
            self.fetch_data()
            
            con.close()


    def academic(self):
        academic = tkinter.messagebox.askyesno("welcome","Do You Want to add the Marks Of the student")
        if academic > 0:

            root.destroy()
            import academic

    def placement(self):
        placement = tkinter.messagebox.askyesno("welcome","Do You Want to add the placement details Of the student")
        if placement > 0:

            root.destroy()
            import placement


    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="students")
        cur=con.cursor()

        cur.execute("select * from std Where " + str(self.search_by.get()) +" Like '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()
            
       
    def logout(self):
        
        logout = tkinter.messagebox.askyesno("TankYou","Do You Really want to LOGOUT")
        if logout > 0:

            root.destroy()
            import login

root = Tk()
ob = Student(root)
root.mainloop()