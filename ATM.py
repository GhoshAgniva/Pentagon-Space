Account_balance = 100000
pin_number = 1234
otp = 4567
daily_limit = 10000

print("WELCOME TO ATM!!!!!!!!")
print("PLEASE INSERT YOUR CARD AND WAIT...........")

while True:  # Loop to allow multiple transactions
    initial_pin = int(input("Enter your pin: "))
    if initial_pin == pin_number:
        print("Press 1: For Withdrawal Money")
        print("Press 2: For checking the balance")
        print("Press 3: For changing the PIN")
        print("Press 4: For fund transfer")
        print("Press 7: For cash deposit")
        print("Press 11: For secure logout")

        initial_key = int(input())

        # WITHDRAWAL MONEY
        if initial_key == 1:
            print("Press 4: Withdraw money from savings account:")
            print("Press 5: Withdraw money from current account:")

            key_press = int(input())
            if key_press == 4:
                withdrawal_amount = int(input("Enter the amount you want to withdraw: "))
                pin_input = int(input("Enter your four-digit PIN number: "))
                if withdrawal_amount > Account_balance:
                    print("You have insufficient balance")
                elif withdrawal_amount <= daily_limit:
                    if pin_input == pin_number:
                        Account_balance -= withdrawal_amount
                        print("Please wait for cash: Cash withdrawn")
                        receipt = input("Do you want a receipt? (yes/no): ")
                        if receipt.lower() == "yes":
                            print(f'''
                            Children's Bank of India
                            | --------------------------------------------------------------------------|
                            | Your current balance:    {Account_balance}            |
                            | Money Withdrawn: {withdrawal_amount}                                      |
                            |                                                                           |
                            |                  Thank you for visiting                                    |
                            | --------------------------------------------------------------------------|
                            ''')
                    else:
                        print("Invalid PIN")
                else:
                    print("Please enter your OTP:")
                    otp_input = int(input())
                    if otp_input == otp:
                        Account_balance -= withdrawal_amount
                        print("Cash withdrawal")
                        print("Remaining balance: ", Account_balance)
                        receipt = input("Do you want a receipt? (yes/no): ")
                        if receipt.lower() == "yes":
                            print(f'''
                            Children's Bank of India
                            | --------------------------------------------------------------------------|
                            | Your current balance:    {Account_balance}            |
                            | Money Withdrawn: {withdrawal_amount}                                      |
                            |                                                                           |
                            |                  Thank you for visiting                                    |
                            | --------------------------------------------------------------------------|
                            ''')
                    else:
                        print("Invalid OTP")

            elif key_press == 5:
                withdrawal_amount = int(input("Enter the amount you want to withdraw: "))
                pin_input = int(input("Enter your four-digit PIN number: "))
                if pin_input == pin_number:
                    if withdrawal_amount <= Account_balance:
                        Account_balance -= withdrawal_amount
                        print("Please wait for cash: Cash withdrawn")
                        receipt = input("Do you want a receipt? (yes/no): ")
                        if receipt.lower() == "yes":
                            print(f'''
                            Children's Bank of India
                            | --------------------------------------------------------------------------|
                            | Your current balance:    {Account_balance}            |
                            | Money Withdrawn: {withdrawal_amount}                                      |
                            |                                                                           |
                            |                  Thank you for visiting                                    |
                            | --------------------------------------------------------------------------|
                            ''')
                    else:
                        print("You have insufficient funds in your account")
                else:
                    print("Invalid PIN")

        # Checking Account Balance
        elif initial_key == 2:
            Balance_checking_key = int(input("Enter your four-digit PIN: "))
            if Balance_checking_key == pin_number:
                print("Your Available balance is: ", Account_balance)

        # Changing PIN
        elif initial_key == 3:
            existing_pin = int(input("Enter the previous password: "))
            if existing_pin == pin_number:
                new_pin = int(input("Enter your new password: "))
                pin_number = new_pin  # Update the pin_number variable with the new PIN
                print("Your PIN has been updated.")
            else:
                print("Invalid Password")

        # Fund Transfer
        elif initial_key == 4:
            transfer_amount = int(input("Enter the amount you want to transfer: "))
            if transfer_amount > Account_balance:
                print("You have insufficient funds")
            elif transfer_amount <= 0:
                print("Invalid input")
            else:
                recipient_account = input("Enter the recipient's account number: ")
                print(f"Transfer successful! {transfer_amount} transferred to account {recipient_account}")
                Account_balance -= transfer_amount
                print("Remaining balance: ", Account_balance)




        # Cash Deposit
        elif initial_key == 7:
            deposite_amount=int(input("Enter the deposite amount: "))
            if deposite_amount==0:
                print("Invalid input")
            else:
                print("Your money is deposited")
                Account_balance=Account_balance+deposite_amount
                print(f"your current balance is:{Account_balance}")



        # Secure Logout
        elif initial_key == 11:
            print("Logout successful. Have a nice day!")
            break

        else:
            print("Invalid option. Please try again.")

    else:
        print("Invalid PIN. Please try again.")
