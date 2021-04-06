from tkinter import*
from tkinter import messagebox,ttk
import pymysql

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)
        #frame
        Frame_login=Frame(self.root,bg="black")
        Frame_login.place(x=150,y=150,height=340,width=500)

        title=Label(Frame_login,text="login Here",font=("Impact",35,"bold"),fg="white",bg="black").place(x=90,y=30)
        desc=Label(Frame_login,text="Accountant Employee Login Area",font=("Goudy old style",15,"bold"),fg="white",bg="black").place(x=90,y=100)
        lbl_Email=Label(Frame_login,text="Email ID",font=("Goudy old style",15,"bold"),fg="gray",bg="black").place(x=90,y=140)
        self.txt_Email=Entry(Frame_login,font=("times new roman",15 ),bg="lightgray")
        self.txt_Email.place(x=90,y=170,width=350,height=35)

        lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="black").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15 ),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        forget_btn=Button(Frame_login,text="Forget Password?",command=self.forget_password,cursor="hand2",bg="black",fg="red",bd=0,font=("times new roman",12)).place(x=260,y=280)
        register_btn=Button(Frame_login,text="Register New Account?",command=self.register_window,cursor="hand2",bg="black",fg="red",bd=0,font=("times new roman",12)).place(x=90,y=280)
        Login_btn=Button(self.root,command=self.login_function ,cursor="hand2",text="Login",bg="black",fg="white",font=("times new roman",20)).place(x=300,y=470,width=180,height=40)
    
    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass.delete(0,END)
        self.txt_Email.delete(0,END)   
    def forget_pass(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from emp where Email=%s and question=%s and answer=%s",(self.txt_Email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select Correct Security Question / Enter  Answer",parent=self.root2)

                else:
                    cur.execute("update emp set password=%s Where email=%s",(self.txt_new_pass.get(),self.txt_Email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your password has been reset",parent=self.root2)                  
                    self.reset()
                    self.root2.destroy()
                    
            
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
        
        
    def forget_password(self):
        if self.txt_Email.get()=="":
            messagebox.showerror("Error","Please enter address to reset your password",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from emp where Email=%s",self.txt_Email.get())
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter the valid address to reset your password",parent=self.root)

                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+480+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)

                    question=Label(self.root2,text="Security question",font=("times new roman",15,"bold"),bg="white").place(x=50,y=100)
            
                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly',justify=CENTER)
                    self.cmb_quest['values']=("Select","Your Pet Name","Your Birth Place","Your Best Friend Name")
                    self.cmb_quest.place(x=50,y=130,width=250)
                    self.cmb_quest.current(0)
                    
                    answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=180)    
                    self.txt_answer=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_answer.place(x=50,y=210,width=250)

                    new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=260)    
                    self.txt_new_pass=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_new_pass.place(x=50,y=290,width=250)

                    btn_change_password=Button(self.root2,text="Reset Password",command=self.forget_pass,bg="green",fg="white",font=("times new roman",15,"bold")).place(x=90,y=340)
                                    

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
    
            
         
        
    
    
    def register_window(self):
        self.root.destroy()
        import register        

    
    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_Email.get()=="": 
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from emp where Email=%s and password=%s",(self.txt_Email.get(),self.txt_pass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username or Password",parent=self.root)
    
                else:
                    messagebox.showinfo("Success","Welcome",parent=self.root)
                    self.root.destroy()
                    import Student
                    con.close()                    

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)


root=Tk()   

obj=Login(root)
root.mainloop()