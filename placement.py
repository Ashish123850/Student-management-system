from tkinter import *
from tkinter import ttk
import pymysql
import tkinter.messagebox
from tkinter import messagebox

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1420x800+0+0")

        title = Label(self.root, text="Students Management System", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="#f3ca20", fg="black")
        title.pack(side=TOP, fill=X)

        # all variable
        self.Batch_var = StringVar()
        self.Department_var = StringVar()
        self.Name_var = StringVar()
        self.Company_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        # Manage Frame
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#f3ca20")
        Manage_Frame.place(x=40, y=100, width=550, height=620)

        m_title = Label(Manage_Frame, text="Placement Details", bg="#f3ca20", fg="black",
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

        lbl_Name = Label(Manage_Frame, text="Name", bg="#f3ca20", fg="black", font=("times new roman", 15, "bold"))
        lbl_Name.grid(row=3, column=0, pady=5, padx=20, sticky="w")

        
        txt_Name = Entry(Manage_Frame,textvariable=self.Name_var,font=("times new roman", 12, "bold"), bd=5,relief=GROOVE)
        txt_Name.grid(row=3, column=1, padx=20, pady=5, sticky="w")
        
        lbl_Company = Label(Manage_Frame, text="Company", bg="#f3ca20", fg="black", font=("times new roman", 15, "bold"))
        lbl_Company.grid(row=4, column=0, pady=5, padx=20, sticky="w")

        combo_Company = ttk.Combobox(Manage_Frame,textvariable=self.Company_var, font=("times new roman", 13, "bold"), state='readonly',justify=CENTER)
        combo_Company['values'] = ("Select","Godrej","WIPRO","HCL","ATOS","TATA","Mastek","inTarvo","Havells","hp","L&T Infotech","Infosys","IBM","Bharat Bijlee")
        combo_Company.grid(row=4, column=1, padx=20, pady=5)
        combo_Company.current(0)
        


    
        # button frame
        btn_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#f3ca20")
        btn_Frame.place(x=40, y=720, width=1360,height=70)
        
    
        Addbtn = Button(btn_Frame, text="Add", width=20,height=2, command=self.add_students,font=("",10,"bold")).grid(row=0, column=0, padx=20,pady=6)
        Updatebtn = Button(btn_Frame, text="Update", width=20,height=2,command=self.update_data,font=("",10,"bold")).grid(row=0, column=1, padx=10, pady=6)
        deletebtn = Button(btn_Frame, text="Delete", width=20,height=2,command=self.delete_data,font=("",10,"bold")).grid(row=0, column=2, padx=10, pady=6)
        Clearbtn = Button(btn_Frame,text="Clear", width=20,height=2,command=self.clear,font=("",10,"bold")).grid(row=0, column=3, padx=10, pady=6)
        Exitbtn = Button(btn_Frame, text="Exit",width=20,height=2,command=self.Exit,font=("",10,"bold")).grid(row=0, column=4, padx=10, pady=6)
        Logoutbtn = Button(btn_Frame, text="Logout",bg="gray",fg="red",bd=5,command=self.logout,width=18,height=2,font=("",10,"bold")).grid(row=0, column=5, padx=200, pady=6)
        
# detail Frame

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#f3ca20")
        Detail_Frame.place(x=600, y=100, width=800, height=590)


        lbl_search = Label(Detail_Frame, text="Search By", bg="#f3ca20", fg="black",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, width=10,textvariable=self.search_by,font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("Department","Name","Batch")
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
        self.Student_table = ttk.Treeview(Table_Frame,columns=("Batch","Department","Name","Company"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        



        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("Batch",text="Batch")
        self.Student_table.heading("Department",text="Department")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("Company",text="Company")
        self.Student_table['show'] = 'headings'
        self.Student_table.column("Batch", width=100)
        self.Student_table.column("Department", width=140)
        self.Student_table.column("Name", width=100)
        self.Student_table.column("Company", width=100)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()
    
        display_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="#f3ca20")
        display_Frame.place(x=228, y=525, width=280, height=56)

        Displaybtn = Button(display_Frame, text="Display Chart of Placement",width=32,height=2,command=self.Display,font=("",10,"bold")).grid(row=0, column=4, padx=4, pady=2)
    
    
    def add_students(self):
        if  self.Company_var.get()=="" or self.Name_var.get()=="":
            messagebox.showerror("Error","All Fields are required")
        elif self.Batch_var.get()=="" or self.Department_var.get()=="":
            messagebox.showerror("Error","All Fields are required")   
        else:
            con = pymysql.connect(host="localhost", user="root", password="",database="placement")
            cur = con.cursor()
            cur.execute("insert into place value(%s,%s,%s,%s)",(self.Batch_var.get(),
                                                            self.Department_var.get(),
                                                            self.Name_var.get(),
                                                            self.Company_var.get()
                                                            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")

    
    
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="placement")
        cur=con.cursor()
        cur.execute("select * from place")
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
            self.Name_var.set("")
            self.Company_var.set("")

    
    
      
    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        content=self.Student_table.item(cursor_row)
        row=content['values']
        self.Batch_var.set(row[0])
        self.Department_var.set(row[1])
        self.Name_var.set(row[2])
        self.Company_var.set(row[3])
        

    def update_data(self):
        self.Batch_var.get()
        self.Department_var.get()
        self.Name_var.get()
        self.Company_var.get()
        if self.Company_var.get()=="" or self.Name_var.get()=="":
          messagebox.showerror("Error","Select the record")
        elif self.Batch_var.get()=="":
          messagebox.showerror("Error","Select the record")
        
        else:
           con = pymysql.connect(host="localhost", user="root", password="", database="placement")
           cur = con.cursor()
           cur.execute("update place set Batch=%s,Department=%s,Name=%s,Company=%s",(
                                                                            self.Batch_var.get(),
                                                                            self.Department_var.get(),
                                                                            self.Name_var.get(),
                                                                            self.Company_var.get()
                                                                            ))
        con.commit()
        messagebox.showinfo("Success","Record has updated Successfully")                
        
        
        self.fetch_data()
        self.clear()
        con.close()
    
   
    def delete_data(self):
        self.Batch_var.get()
        self.Department_var.get()
        self.Name_var.get()
        self.Company_var.get()
        if self.Company_var.get()=="" or self.Name_var.get()=="":
            messagebox.showerror("Error","Select the record")
        
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="placement")
            cur=con.cursor()
            delete = tkinter.messagebox.askyesno("Delete","Do you want to Delete the record")
            if delete > 0:
                cur.execute("delete from place Where Name=%s",self.Name_var.get())
                
                messagebox.showinfo("Success","Record has deleted Successfully")
                self.clear()
        
            con.commit()
            self.fetch_data()
            
            con.close()


    def Exit(self):
        Exit = tkinter.messagebox.askyesno("TankYou","Do You Want to go back to student personal details page")
        if Exit > 0:

            root.destroy()
            import Student

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="placement")
        cur=con.cursor()

        cur.execute("select * from place Where " + str(self.search_by.get()) +" Like '%"+str(self.search_txt.get())+"%'")
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
    def Display(self):
        
        Display = tkinter.messagebox.askyesno("TankYou","Do You want to view the chart")
        if Display > 0:

            root.destroy()
            import chart1
    
root = Tk()
ob = Student(root)
root.mainloop()