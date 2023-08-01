# Bank Management System

This is a simple bank management system implemented using the Python `tkinter` library for the graphical user interface. It allows users to create, view, deposit, withdraw, and delete bank accounts. Account details are stored in a text file named `bank_accounts.txt`.

## Getting Started

1. Make sure you have Python installed on your system.
2. Install the required packages using `pip`:
   ```
   pip install tkinter pillow
   ```

## Features

1. **Create Account**: Users can create a new bank account by entering the account number, name, and initial balance. The system ensures that the account number provided is unique by checking against existing account numbers stored in the `bank_accounts.txt` file.

2. **View Account Details**: Users can view the details of an existing account by entering the account number and clicking the "View Account" button. The system retrieves the account information from the `bank_accounts.txt` file and displays a pop-up window showing the account number, account holder's name, and the current balance.

3. **Deposit Money**: Users can deposit money into an existing account by providing the account number and the amount to deposit. The system validates the input to ensure that the provided amount is a valid numeric value. If the account number is found, the system updates the account balance and saves the changes to the `bank_accounts.txt` file.

4. **Withdraw Money**: Users can withdraw money from an existing account by providing the account number and the amount to withdraw. The system validates the input to ensure that the provided amount is a valid numeric value. Before processing the withdrawal, the system checks if the account has sufficient balance. If the balance is enough, the system updates the account balance and saves the changes to the `bank_accounts.txt` file. Otherwise, it displays an error message indicating insufficient balance.

5. **Delete Account**: Users can delete an existing account by entering the account number and clicking the "Delete Account" button. The system searches for the account number in the `bank_accounts.txt` file. If the account is found, it removes the corresponding account information from the file and saves the updated information. If the account number is not found, the system displays an error message indicating that the account does not exist.

6. **View All Accounts**: Users can view all existing accounts by clicking the "View All Accounts" button. The system reads the contents of the `bank_accounts.txt` file and displays all account information in a new window. A scrollbar is provided for easy navigation through the list of accounts.

7. **Exit Application**: Users can exit the application by clicking the "Exit" button. This terminates the program and closes the application window.

Note: The application uses the `tkinter` library for the graphical user interface and the `PIL` (Python Imaging Library) for working with images. Users can customize the application's appearance, error handling, and file storage as per their specific requirements.

## How to Use

1. Run the script using Python:
   ```
   python main.py
   ```
   The application window will appear with a welcome page. Click the "Start" button to proceed to the main page.

## Author

- Soham Vaity CO- Batch 3

## Data Storage

Account details are stored in a text file named `bank_accounts.txt`. Each line in the file represents an account and follows the format `account_number,name,balance`.

**Note**: This is a simple bank management system intended for learning and demonstration purposes. In real-world scenarios, additional security measures and data validation would be necessary to ensure the system's robustness and security.
