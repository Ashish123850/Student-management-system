from tkinter import*
from tkinter import ttk,messagebox
import pymysql

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registeration Window")
        self.root.geometry("1350x700+0+0")
        
        #left side
        frame=Frame(self.root,bg="gray")
        frame.place(x=80,y=100,width=400,height=500)
        title=Label(frame,text="STUDENT",font=("times new roman",30,"bold"),bg="gray").place(x=30,y=60)    
        title=Label(frame,text="MANAGEMENT",font=("times new roman",30,"bold"),bg="gray").place(x=30,y=105) 
        title=Label(frame,text="SYSTEM",font=("times new roman",30,"bold"),bg="gray").place(x=30,y=150)    
           
        
        Text=Label(frame,text="Dont have Account,",font=("times new roman",20,"bold"),bg="gray",fg="red").place(x=40,y=270)
        Text=Label(frame,text="Register as a new user",font=("times new roman",20,"bold"),bg="gray",fg="red").place(x=80,y=300)

        ##Register frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)    
        

        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=100)    
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)


        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=100)    
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

#------------------------------------

        Contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=170)    
        self.txt_Contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_Contact.place(x=50,y=200,width=250)
        

        Email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=170)    
        self.txt_Email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_Email.place(x=370,y=200,width=250)

        #------------------------------------


        question=Label(frame1,text="Security question",font=("times new roman",15,"bold"),bg="white").place(x=50,y=240)
  
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Select","Your Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)
        
        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=240)    
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)

#----------
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=310)    
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)


        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=310)    
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)

#-------------term
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",fg="black",font=("times new roman",15)).place(x=50,y=380)

        btn_register=Button(frame1,name="submit",text="Register Now",cursor="hand2",font=("times new roman",20),command=self.register_data).place(x=150,y=450,width=180,height=40)

        btn_login=Button(self.root,text="Sign In",comman=self.login_window,font=("times new roman",20),bd=0,cursor="hand2").place(x=200,y=460,width=150)
  



    def login_window(self):
        self.root.destroy()
        import login            

        
    def clear(self):
            self.txt_fname.delete(0,END)
            self.txt_lname.delete(0,END)
            self.txt_Contact.delete(0,END)
            self.txt_Email.delete(0,END)
                
            self.txt_answer.delete(0,END)
            self.txt_password.delete(0,END)
            self.txt_cpassword.delete(0,END)
            self.cmb_quest.current(0)
        
            
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_Contact.get()=="" or self.txt_Email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
           messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif len(self.txt_password.get())!=8:
                messagebox.showerror("error","legth should be more than 8")
        elif self.txt_password.get()!= self.txt_cpassword.get():
           messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0:
           messagebox.showerror("Error","Select Terms & Condition",parent=self.root )
        elif len(self.txt_Contact.get())!=10:

                messagebox.showerror("error","please enter correct number")       
        else:   
             try:
                        con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                        cur=con.cursor()
                        cur.execute("select * from emp where email=%s",self.txt_Email.get())
                        row=cur.fetchone()
                     
                        if row!=None:
                                 messagebox.showerror("Error","User Already Exist,Try with another email",parent=self.root )

                        else:

                                cur.execute("insert into emp (f_name,L_name,contact,Email,question,answer,password)values(%s,%s,%s,%s,%s,%s,%s)",
                                        (self.txt_fname.get(),
                                        self.txt_lname.get(),
                                        self.txt_Contact.get(),
                                        self.txt_Email.get(),
                                        self.cmb_quest.get(),
                                        self.txt_answer.get(),
                                        self.txt_password.get(),
                                        ))
                                con.commit()
                                con.close()
                                messagebox.showinfo("Success","Register Successfull",parent=self.root) 
                                self.clear()

             except Exception as es:        
                  messagebox.showerror("Error", f"Error due to:{str(es)}",parent=self.root )
              
             
             


root=Tk()
ob=Register(root)
root.mainloop()