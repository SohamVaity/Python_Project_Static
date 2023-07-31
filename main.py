import tkinter as tk
from tkinter import messagebox

# Function to check if account number already exists

def account_exists(account_no):
    with open("bank_accounts.txt", "r") as file:
        for line in file:
            if line.startswith(account_no):
                return True
        return False

# Function to save user input to a text file
def save_to_file(account_no, name, balance):
    with open("bank_accounts.txt", "a") as file:
        file.write(f"{account_no},{name},{balance}\n")

# Function to create a new account
def create_account():
    account_no = account_no_entry.get()
    name = name_entry.get()
    balance = balance_entry.get()

    try:
        balance = float(balance)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric balance.")
        return

    if not account_no.strip() or not name.strip():
        messagebox.showerror("Invalid Input", "Account number and name cannot be empty.")
        return

    if account_exists(account_no):
        messagebox.showerror("Account Exists", "An account with this account number already exists.")
        return

    save_to_file(account_no, name, balance)
    messagebox.showinfo("Account Created", "Account created successfully!")

# Function to view account details
def view_account():
    account_no = account_no_entry.get()

    if not account_no.strip():
        messagebox.showerror("Invalid Input", "Please enter an account number.")
        return

    with open("bank_accounts.txt", "r") as file:
        for line in file:
            if line.startswith(account_no):
                acc_info = line.strip().split(',')
                messagebox.showinfo("Account Details", f"Account Number: {acc_info[0]}\nName: {acc_info[1]}\nBalance: {acc_info[2]}")
                return
        messagebox.showerror("Account Not Found", "Account with this account number not found.")

# Function to deposit money into an account
def deposit():
    account_no = account_no_entry.get()

    if not account_no.strip():
        messagebox.showerror("Invalid Input", "Please enter an account number.")
        return

    amount = float(balance_entry.get())

    with open("bank_accounts.txt", "r") as file:
        lines = file.readlines()

    with open("bank_accounts.txt", "w") as file:
        for line in lines:
            if line.startswith(account_no):
                acc_info = line.strip().split(',')
                balance = float(acc_info[2])
                balance += amount
                line = f"{acc_info[0]},{acc_info[1]},{balance}\n"
            file.write(line)

    messagebox.showinfo("Deposit Successful", f"Deposited {amount} into the account.")

# Function to withdraw money from an account
def withdraw():
    account_no = account_no_entry.get()

    if not account_no.strip():
        messagebox.showerror("Invalid Input", "Please enter an account number.")
        return

    amount = float(balance_entry.get())

    with open("bank_accounts.txt", "r") as file:
        lines = file.readlines()

    with open("bank_accounts.txt", "w") as file:
        for line in lines:
            if line.startswith(account_no):
                acc_info = line.strip().split(',')
                balance = float(acc_info[2])
                if balance >= amount:
                    balance -= amount
                    line = f"{acc_info[0]},{acc_info[1]},{balance}\n"
                else:
                    messagebox.showerror("Insufficient Balance", "Not enough balance in the account.")
                    return
            file.write(line)

    messagebox.showinfo("Withdrawal Successful", f"Withdrew {amount} from the account.")

# Function to delete an account
def delete_account():
    account_no = account_no_entry.get()

    if not account_no.strip():
        messagebox.showerror("Invalid Input", "Please enter an account number.")
        return

    with open("bank_accounts.txt", "r") as file:
        lines = file.readlines()

    deleted = False
    with open("bank_accounts.txt", "w") as file:
        for line in lines:
            if not line.startswith(account_no):
                file.write(line)
            else:
                deleted = True

    if deleted:
        messagebox.showinfo("Account Deleted", "Account successfully deleted.")
    else:
        messagebox.showerror("Account Not Found", "Account with this account number not found.")

# Function to exit the application
def exit_app():
    root.destroy()

# Creating the tkinter window
root = tk.Tk()
root.title("Bank Management System")

# Labels
account_no_label = tk.Label(root, text="Account Number:")
account_no_label.grid(row=0, column=0)
name_label = tk.Label(root, text="Name:")
name_label.grid(row=1, column=0)
balance_label = tk.Label(root, text="Balance:")
balance_label.grid(row=2, column=0)

# Entry fields
account_no_entry = tk.Entry(root)
account_no_entry.grid(row=0, column=1)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1)
balance_entry = tk.Entry(root)
balance_entry.grid(row=2, column=1)

# Create Account Button
create_btn = tk.Button(root, text="Create Account", command=create_account)
create_btn.grid(row=3, column=0, columnspan=2)

# View Account Details Button
view_btn = tk.Button(root, text="View Account", command=view_account)
view_btn.grid(row=4, column=0, columnspan=2)

# Deposit Button
deposit_btn = tk.Button(root, text="Deposit", command=deposit)
deposit_btn.grid(row=5, column=0, columnspan=2)

# Withdraw Button
withdraw_btn = tk.Button(root, text="Withdraw", command=withdraw)
withdraw_btn.grid(row=6, column=0, columnspan=2)

# Delete Account Button
delete_btn = tk.Button(root, text="Delete Account", command=delete_account)
delete_btn.grid(row=7, column=0, columnspan=2)

# Exit Button
exit_btn = tk.Button(root, text="Exit", command=exit_app)
exit_btn.grid(row=8, column=0, columnspan=2)

root.mainloop()
