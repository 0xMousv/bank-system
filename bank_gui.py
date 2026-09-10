import tkinter as tk
from tkinter import messagebox
users = {}
window = tk.Tk()
window.title("Simple Bank")
window.geometry("400x450")

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

def signup():
    clear_window()
    tk.Label(window,text="Create New Account",font=20).pack()
    tk.Label(window,text="Username",font=15).pack()
    username = tk.Entry(window)
    username.pack()
    tk.Label(window,text="password",font=15).pack()   
    password = tk.Entry(window,show="*")
    password.pack()
    tk.Label(window,text="Balance",font=15).pack()
    balan = tk.Entry(window)
    balan.pack()
    def create_account():
        user=username.get()
        passwd = password.get()
        balance = float(balan.get())
        if user in users:
            messagebox.showerror("Error", "This User is used")
        elif user == "" or passwd == "":
            messagebox.showerror("Error", "please fill the boxs)
        else:
            users[user] = { "password": passwd, "balance": balance, "transactions": [] }
            messagebox.showinfo("Creating accout Succses" , f"Welcome ,{user}")
            main()
            print(users)
    button=tk.Button(window,text="Sing Up", command=create_account)
    button.pack()

def login():
    clear_window()
    tk.Label(window,text="Username",font=15).pack()
    username = tk.Entry(window)
    username.pack()
    tk.Label(window,text="password",font=15).pack()   
    password = tk.Entry(window,show="*")
    password.pack()
    def log():
        user=username.get()
        passwd = password.get()
        if user in users:
            if passwd == users[user]["password"]:
                print("7beb den omy")
                messagebox.showinfo("login","login succses")
                dashboard(user)
            else:
                messagebox.showerror("","login faild")
        else:
            messagebox.showerror("","login faild")
    
    tk.Button(window,text="Login",command=log).pack()

def dashboard(user):
    clear_window()

    tk.Label(window,text=f"Welcome , {user}" , font=20).pack()
    tk.Button(window,text="Deposit",command=lambda:deposit(user)).pack()
    tk.Button(window,text="Withdraw",command=lambda:withdraw(user)).pack()
    tk.Button(window,text="transfar",command=lambda:transfar(user)).pack()
    tk.Button(window,text="Account Check",command=lambda:check(user)).pack()
    tk.Button(window,text="History transfer",command=lambda:history(user)).pack()
    tk.Button(window,text="Channge Passowrd",command=lambda:change(user)).pack()
    tk.Button(window,text="Logout",command=logout).pack()
    
def deposit(user):
    clear_window()
    tk.Label(window,text=f"Welcome , {user}" , font=20).pack()
    tk.Label(window,text="Enter Deposit",font=15).pack()
    dp = tk.Entry(window)
    dp.pack()
    def add():
        deposited = float(dp.get())
        if deposited <= 0:
            messagebox.showerror("Error","Add Num Against 0") 
        users[user]['balance'] += deposited
        users[user]['transactions'].append(f"Deposit +${deposited}")
        messagebox.showinfo("New Balance", f"your new balance: {users[user]['balance']}")
    tk.Button(window,text="Deposit",command=add).pack()
    tk.Button(window,text="Back To Dashboard",command=lambda: dashboard(user)).pack()

def withdraw(user):
    clear_window()
    tk.Label(window,text=f"Welcome , {user}" , font=20).pack()
    tk.Label(window,text="Enter Witdraw",font=15).pack()
    wd = tk.Entry(window)
    wd.pack()
    def plus():
        withdrawed= float(wd.get())
        users[user]['balance'] -= withdrawed
        users[user]['transactions'].append(f"Withdraw -${withdrawed}")
        messagebox.showinfo("succese", f"your New Balance: ${users[user]['balance']}")

    tk.Button(window,text="witdraw",command=plus).pack()
    tk.Button(window,text="Back To Dashboard",command=lambda:dashboard(user)).pack()

def transfar(user):
    clear_window()
    tk.Label(window,text=f"Welcome , {user}" , font=20).pack()
    tk.Label(window,text="Enter User to Transfar",font=15).pack()
    tran = tk.Entry(window)
    tran.pack()
    tk.Label(window,text="Ammount Transfar",font=15).pack()
    transed = tk.Entry(window)
    transed.pack()
    def trans():
        transfared_user = tran.get()
        transed_amount = float(transed.get())
        if  transfared_user not in users:
            messagebox.showerror("error","user is not found")
        elif transfared_user == user:
            messagebox.showerror("error","You Cant Transfar to your self")
        elif transed_amount == 0:
            messagebox.showerror("error", "you cant trans 0 please add bigger than 0")
        elif users[user]['balance'] == 0:
            messagebox.showerror('Error', "You dont have Enough Money")
        else:
            users[user]['balance'] -= transed_amount
            users[transfared_user]['balance'] += transed_amount
            users[user]['transactions'].append(f"Transfar -${transed_amount} to {transfared_user}")
            users[transfared_user]['transactions'].append(f"transfar +${transed_amount} from {user}")
            messagebox.showinfo("Succses",f"your new balance is : {users[user]['balance']}")
    tk.Button(window,text="Transefar",command=trans).pack()
    tk.Button(window,text="back",command=lambda:dashboard(user)).pack()
def check(user):
    messagebox.showinfo("your info", f"{users[user]}")
def history(user):
    messagebox.showinfo("your histroy", f"{users[user]['transactions']}")
def change(user):
    clear_window()
    tk.Label(window,text="Change Your password",font=20).pack()
    tk.Label(window,text="Current Password",font=15).pack()
    currnt_password = tk.Entry(window,show="*")
    currnt_password.pack()
    tk.Label(window,text="New Password",font=15).pack()
    new = tk.Entry(window,show="*")
    new.pack()
    tk.Label(window,text="Confirem password",font=15).pack()
    re_new = tk.Entry(window,show="*")
    re_new.pack()
    def changing():
        currnt = currnt_password.get()
        new_pass = new.get()
        re_new_pass = re_new.get()
        if currnt == users[user]['password']:
            if new_pass == re_new_pass:
                users[user]['password'] = new_pass
                login()
                messagebox.showinfo("Succes","Password Was changing")
            else:
                messagebox.showerror("error","New Password != re new")       
        else:
            messagebox.showerror("error","password is wrong")
    tk.Button(window,text="Confirm",command=changing).pack()
def logout():
    main()
        
def main():
    clear_window()
    tk.Label(window,text="Welcome To Our Bank",font=20).pack()
    tk.Button(window,text="Sign Up",command=signup).pack()
    tk.Button(window,text="Login",command=login).pack()
    tk.Button(window,text="exit",command=exit).pack()
main()
window.mainloop()
