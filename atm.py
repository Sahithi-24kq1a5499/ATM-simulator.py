# Simple ATM Machine Program

balance = 5000 # starting balance
pin = "1234" # default pin

print("Welcome to ATM Machine")

# PIN check
entered_pin = input("Enter your 4-digit PIN: ")
if entered_pin != pin:
    print("Incorrect PIN. Exiting...")
else:
    while True:
        print("\n--- ATM Menu ---")
        print("1. Balance Inquiry")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print(f"Your current balance is ₹{balance}")

        elif choice == "2":
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance!")
            else:
                balance -= amount
                print(f"Please collect ₹{amount}")
                print(f"Remaining Balance: ₹{balance}")

        elif choice == "3":
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print(f"Deposited ₹{amount}")
            print(f"New Balance: ₹{balance}")

        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
