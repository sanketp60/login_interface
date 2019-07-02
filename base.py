from tkinter import *
from tkinter import messagebox
file=open("database", "a")
file.close()
def check_already(id):
    with open('database') as fp:
        for line in fp:
            if line.split('%#20%')[0]==id:
                return 1            
user="NULL"
def app_window():
    mainwindow=Tk()
    mainwindow.title("Main App")
    lb=Label(mainwindow, text="Hello "+user+", you are logged-in successfully!").pack()
    def control_logout():
        loginwindow.deiconify()
        mainwindow.destroy()
    logout=Button(mainwindow, text="Logout", command=control_logout).pack()
    mainwindow.mainloop()
def create_window():
    createwindow=Toplevel()
    createwindow.grab_set()
    createwindow.title("Creating user")
    createwindow.resizable(0,0)
    id=StringVar()
    id.set("")
    pswd_new=StringVar()
    pswd_new.set("")
    idlbl=Label(createwindow, text="ID").grid(row=0, column=0)
    identry=Entry(createwindow, textvariable=id, width=30).grid(row=0, column=1)
    pswdlbl=Label(createwindow, text="Password").grid(row=1, column=0)
    pswdentry=Entry(createwindow, textvariable=pswd_new, show="•", width=30).grid(row=1, column=1)
    def make_user():
        if check_already(id.get())!=1 and pswd.get!=(""):
            cred_file=open("database", "a")
            cred_file.write(id.get()+"%#20%"+pswd_new.get()+"\n")
            cred_file.close()
            messagebox.showinfo("Success", "New user is created")
            createwindow.destroy()
        else:
            messagebox.showerror("Create Error","ID already in use or Invalid Credentials")
    submit=Button(createwindow, text="Submit", command=make_user).grid(row=2, columnspan=2)
    createwindow.mainloop()
def checker(id, pswd):
    with open('database') as fp:
        for line in fp:
            if line.split('%#20%')[0]==id  and line.split('%#20%')[1].replace("\n", "")==pswd:
                return 1
loginwindow=Tk()
loginwindow.title("Login")
loginwindow.resizable(0,0)
id=StringVar()
id.set("")
pswd=StringVar()
pswd.set("")
checkbox_var=IntVar()
idlbl=Label(loginwindow, text="ID").grid(row=0, column=0)
identry=Entry(loginwindow, textvariable=id, width=30).grid(row=0, column=1)
pswdlbl=Label(loginwindow, text="Password").grid(row=1, column=0)
pswdentry=Entry(loginwindow, textvariable=pswd, show="•", width=30).grid(row=1, column=1)  
def control_login():
    if checker(id.get(),pswd.get()) == 1 and id.get()!="" and pswd.get()!="":
        global user
        loginwindow.withdraw()
        user=id.get()
        if checkbox_var.get() == 0:
            id.set("")
            pswd.set("")
        app_window() 
    else:
        messagebox.showerror("Login Error","Invalid Credentials")      
checkbutton=Checkbutton(loginwindow, text="Remember me", variable=checkbox_var).grid(row=2, columnspan=2)
login=Button(loginwindow, text="Login", command=control_login).grid(row=3, columnspan=2)
create=Button(loginwindow, text="Create account", command=create_window).grid(row=4, columnspan=2)
loginwindow.mainloop()
