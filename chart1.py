from tkinter import *
from tkinter import ttk
import pymysql
import tkinter.messagebox
from tkinter import messagebox

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1400x800+0+0")

        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="#f3ca20", fg="black")
        title.pack(side=TOP, fill=X)

        # all variable
        self.search_by = StringVar()
        self.search1_by = StringVar()
        self.search2_by = StringVar()
        self.search3_by = StringVar()

        # Manage Frame
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#f3ca20")
        Manage_Frame.place(x=300, y=84, width=800, height=80)

        m_title = Label(Manage_Frame, text="Chart of the Placement", bg="#f3ca20", fg="black",
                        font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, padx=275, pady=10)

         
        
# detail Frame
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#f3ca20")
        Detail_Frame.place(x=300, y=180, width=800, height=598)

        lbl_search = Label(Detail_Frame, text="Search By", bg="#f3ca20", fg="black",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, width=10,textvariable=self.search_by,font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("select","Batch")
        combo_search.grid(row=0, column=1, padx=20, pady=10)
        combo_search.current(0)

        combo_search1 = ttk.Combobox(Detail_Frame, width=10,textvariable=self.search1_by,font=("times new roman", 13, "bold"), state='readonly')
        combo_search1['values'] = ("select","2015-16","2016-17")
        combo_search1.grid(row=0, column=2, padx=20, pady=10)
        combo_search1.current(0)

        
        combo_search2 = ttk.Combobox(Detail_Frame, width=10,textvariable=self.search2_by,font=("times new roman", 13, "bold"), state='readonly')
        combo_search2['values'] = ("select","Company")
        combo_search2.grid(row=1, column=1, padx=20, pady=10)
        combo_search2.current(0)

        combo_search3 = ttk.Combobox(Detail_Frame, width=10,textvariable=self.search3_by,font=("times new roman", 13, "bold"), state='readonly')
        combo_search3['values'] = ("select","wipro","goderj")
        combo_search3.grid(row=1, column=2, padx=20, pady=10)
        combo_search3.current(0)

        searchbtn = Button(Detail_Frame, text="View Chart", width=10, pady=5,command=self.search_data).grid(row=0, column=5, padx=10, pady=10)


    #display frame
        display_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="#f3ca20")
        display_Frame.place(x=700, y=550, width=85, height=40)

        Exitbtn = Button(display_Frame, text="Exit",width=8,height=1,command=self.Exit,font=("",10,"bold")).grid(row=0, column=4, padx=3, pady=2)
    
        ##table frame
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="black")
        Table_Frame.place(x=10, y=100, width=760, height=450)

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
        self.fetch_data()

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
            
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="placement")
        cur=con.cursor()

        cur.execute("select * from place Where " + str(self.search_by.get()) +" Like '%"+str(self.search1_by.get())+"%'")
        
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()
   
    
    def Exit(self):
        
        exit = tkinter.messagebox.askyesno("TankYou","Do You want to student marks page")
        
        if exit > 0:

            root.destroy()
            import placement

        elif exit > 0:

            root.destroy()
            import placement
    
       
    def logout(self):
        
        logout = tkinter.messagebox.askyesno("TankYou","Do You Really want to LOGOUT")
        if logout > 0:

            root.destroy()
            import login

root = Tk()
ob = Student(root)
root.mainloop()