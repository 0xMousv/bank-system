import tkinter as tk

users = {}

def sing():
    username = input("Enter username: ")
    password = input("Enter password: ")
    balance = float(input("Enter User Balance: "))
    users[username]={
        "password": password,
        "balance": balance,
        "transactions": []
    }
    main()


def login():
    for i in range(3):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users:
            if users[username]["password"] == password:
                print("Login Succ")
                print(f"Welcome {username}!")
                dashboard(username)
                return
            else:
                print("Wrong Password")
        else:
            print("User not found")

    print("Account locked y 3m")


def dashboard(username):
     while True:
        print("[1] 💰 Check Balance")
        print("[2] ➕ Deposit Money")
        print("[3] ➖ Withdraw Money")
        print("[4] 🔄 Transfer Money")
        print("[5] 📜 Transaction History")
        print("[6]     Account information")
        print("[7]     Change Password")
        print("[8] ⛔ Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            balance = users[username]["balance"]
            print(f"Your balance is: ${balance}")
        elif choice == "2":
            deposit = float(input("Enter Deposit: "))
            if deposit <= 0:
                print("try again")
            else:
                users[username]["balance"] += deposit
                users[username]["transactions"].append(f"Deposit +${deposit}")
                print(f"Your new balance is: ${users[username]['balance']}")
        elif choice == "3":
            withdraw = float(input("Enter Withdraw: "))
            if users[username]["balance"] >= withdraw:
                users[username]["balance"] -= withdraw
                users[username]["transactions"].append(f"Withdraw -${withdraw}")
                print(f"Your new balance is: {users[username]["balance"]}")
            else:
                print("u dont have enough money ya S7at")
        elif choice == "4":
            trans_user = input("Enter User to Transfer: ")
            trans_balance = float(input("Enter Balance: "))
            if trans_user in users:
                if trans_user == username:
                    print("You can't transfer money to yourself.")
                elif trans_balance > users[username]["balance"]:
                    print("Insufficient balance.")

                elif trans_balance <= 0:
                    print("Amount must be greater than 0.")

                else:
                    users[username]["balance"] -= trans_balance
                    users[trans_user]["balance"] += trans_balance
                    users[username]["transactions"].append(f"Transfer -${trans_balance} to {trans_user}")
                    users[trans_user]["transactions"].append(f"Transfer +${trans_balance} from {username}")
                    print("Transfer Successful!")
                    print(f"Your new balance: ${users[username]['balance']}")
        elif choice == "5":
            print(f"Your History: {users[username]["transactions"]}")
        elif choice == "6":
            print(f"Your Information : {users[username]}")
        elif choice == "7":
            current = input("Enter Your Current password: ")       
            new = input("Enter Your New Password: ")
            re_new = input("Re-Enter Your New Password: ")
            if current == users[username]["password"]:
                if new == re_new:
                    users[username]["password"] = new
                    print("Password Had Changed")
        elif choice == "8":
            main()
def main():
    print(25 * "=")
    print("  welcome to our bank ")
    print(25 * "=")
    print("[1] Sign Up")
    print("[2] Login")
    print("[3] Exit")
    choice = input("Select Your Option: ")
    if choice == "1":
        sing()
    elif choice == "2":
        login()
    elif choice == "3":
        exit()
    else:
        print("Your Option is Not foun Try Again")
main()
