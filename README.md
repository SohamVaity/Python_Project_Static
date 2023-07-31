# Bank Management System

This is a simple bank management system implemented using the Python `tkinter` library for the graphical user interface. It allows users to create, view, deposit, withdraw, and delete bank accounts. Account details are stored in a text file named `bank_accounts.txt`.

## Features

1. **Create Account**: Users can create a new bank account by entering the account number, name, and initial balance. The account number must be unique.

2. **View Account Details**: Users can view the details of an existing account by entering the account number. The system will display the account number, name, and current balance in a pop-up window.

3. **Deposit Money**: Users can deposit money into an existing account by providing the account number and the amount to deposit. The balance of the account will be updated accordingly.

4. **Withdraw Money**: Users can withdraw money from an existing account by providing the account number and the amount to withdraw. The system will check for sufficient balance before processing the withdrawal.

5. **Delete Account**: Users can delete an existing account by entering the account number. The account will be removed from the system, and the text file will be updated.

## How to Use 

1. Run the script, and a window titled "Bank Management System" will appear.

2. To create a new account, enter the account number, name, and initial balance in the respective fields, then click the "Create Account" button.

3. To view account details, enter the account number and click the "View Account" button. The account details will be displayed in a pop-up window.

4. To deposit money into an account, enter the account number and the amount to deposit, then click the "Deposit" button.

5. To withdraw money from an account, enter the account number and the amount to withdraw, then click the "Withdraw" button. Note that the account must have sufficient balance for the withdrawal to be successful.

6. To delete an account, enter the account number and click the "Delete Account" button. The account will be removed from the system.

7. Click the "Exit" button to close the application.

## Data Storage

Account details are stored in a text file named `bank_accounts.txt`. Each line in the file represents an account and follows the format `account_number,name,balance`.

**Note**: This is a simple bank management system intended for learning and demonstration purposes. In real-world scenarios, additional security measures and data validation would be necessary to ensure the system's robustness and security.
