import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

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

    if not account_no.strip() or not name.strip():
        messagebox.showerror("Invalid Input", "Account number and name cannot be empty.")
        return

    try:
        balance = float(balance)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric balance.")
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

    amount = balance_entry.get()

    if not amount.strip():
        messagebox.showerror("Invalid Input", "Please enter the amount in the balance field.")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")
        return

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

    amount = balance_entry.get()

    if not amount.strip():
        messagebox.showerror("Invalid Input", "Please enter the amount in the balance field.")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")
        return

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

# Function to view all accounts
def view_all_accounts():
    with open("bank_accounts.txt", "r") as file:
        all_accounts = file.read()

    view_all_window = tk.Toplevel(root)
    view_all_window.title("All Accounts")

    scrollbar = tk.Scrollbar(view_all_window, orient=tk.VERTICAL)
    all_accounts_text = tk.Text(view_all_window, wrap=tk.NONE, yscrollcommand=scrollbar.set)
    scrollbar.config(command=all_accounts_text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    all_accounts_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    all_accounts_text.insert(tk.END, all_accounts)

# Function to exit the application
def exit_app():
    root.destroy()

# Creating the tkinter window
root = tk.Tk()
root.title("Bank Management System")
root.geometry("800x600")

# Welcome page
welcome_frame = tk.Frame(root, bg="lightblue")
welcome_frame.pack(fill=tk.BOTH, expand=True)

welcome_label = tk.Label(welcome_frame, text="Welcome to Bank Management System!", font=("Helvetica-Bold", 30), bg="lightblue")
welcome_label.pack(pady=50)

# Add image link to the welcome page
welcome_image = Image.open("VBI.png") 
welcome_image = welcome_image.resize((370, 370))
welcome_image = ImageTk.PhotoImage(welcome_image)
image_label = tk.Label(welcome_frame, image=welcome_image, bg="lightblue")
image_label.pack()

start_btn = tk.Button(welcome_frame, text="Start", command=welcome_frame.pack_forget, bg="lightgreen", width=10)
start_btn.pack(pady=20)

# Main page
main_frame = tk.Frame(root, bg="lightblue")
main_frame.pack(fill=tk.BOTH, expand=True)

# Add image link to the main page
bank_logo = Image.open("Static.png") 
bank_logo = bank_logo.resize((250, 250))
bank_logo = ImageTk.PhotoImage(bank_logo)
logo_label = tk.Label(main_frame, image=bank_logo, bg="lightblue")
logo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Labels
account_no_label = tk.Label(main_frame, text="Account Number:", bg="lightblue")
account_no_label.grid(row=1, column=0, padx=10, pady=5)
name_label = tk.Label(main_frame, text="Name:", bg="lightblue")
name_label.grid(row=2, column=0, padx=10, pady=5)
balance_label = tk.Label(main_frame, text="Balance:", bg="lightblue")
balance_label.grid(row=3, column=0, padx=10, pady=5)

# Entry fields
account_no_entry = tk.Entry(main_frame)
account_no_entry.grid(row=1, column=1, padx=10, pady=5)
name_entry = tk.Entry(main_frame)
name_entry.grid(row=2, column=1, padx=10, pady=5)
balance_entry = tk.Entry(main_frame)
balance_entry.grid(row=3, column=1, padx=10, pady=5)

# Create Account Button
create_btn = tk.Button(main_frame, text="Create Account", command=create_account, bg="lightgreen")
create_btn.grid(row=4, column=0, padx=10, pady=5)

# View Account Details Button
view_btn = tk.Button(main_frame, text="View Account", command=view_account, bg="lightgreen")
view_btn.grid(row=4, column=1, padx=10, pady=5)

# Deposit Button
deposit_btn = tk.Button(main_frame, text="Deposit", command=deposit, bg="lightgreen")
deposit_btn.grid(row=5, column=0, padx=10, pady=5)

# Withdraw Button
withdraw_btn = tk.Button(main_frame, text="Withdraw", command=withdraw, bg="lightgreen")
withdraw_btn.grid(row=5, column=1, padx=10, pady=5)

# Delete Account Button
delete_btn = tk.Button(main_frame, text="Delete Account", command=delete_account, bg="lightcoral")
delete_btn.grid(row=6, column=0, padx=10, pady=5)

# View All Accounts Button
view_all_btn = tk.Button(main_frame, text="View All Accounts", command=view_all_accounts, bg="yellow")
view_all_btn.grid(row=6, column=1, padx=10, pady=5)

# Exit Button
exit_btn = tk.Button(main_frame, text="Exit", command=exit_app, bg="lightcoral")
exit_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
