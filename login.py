from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from subprocess import call


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        #self.bg=ImageTk.PhotoImage(file=r"C:\Users\Sharwari\Desktop\DBMS MINI PROJECT\images\2.jpeg")
        #lbl_bg=Label(self.root,image=self.bg)
        #lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black",)
        frame.place(x=610,y=170,width=340,height=450)

        get_str=Label(frame,text="ADMIN LOGIN",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=80,y=100)

        # Labels
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=50,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=50,y=220)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"), show = "*")
        self.txtpass.place(x=40,y=250,width=270)

        loginbtn=Button(frame,text="Login",command=self.login, font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                con=mysql.connector.connect(host='localhost', username='root',password='Sharwari@21', database='management')
                cur=con.cursor() 
                cur.execute("select * from login where userid=%s and password=%s", (self.txtuser.get(), self.txtpass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid User ID or Password")
                else:
                    messagebox.showinfo("successful", "Welcome") 
                    self.root.destroy()
                    call(['python','crime management system.py'])                  
                con.close()  
            except Exception as er:
                messagebox.showerror('error',f'Due to {str(er)}')   
        

if __name__=="__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()



    

                      