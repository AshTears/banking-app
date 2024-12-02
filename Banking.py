# This project demonstrates an ATM

balance = 56825.37

def get_balance():
    print(f"Your balance is ${balance:.2f}")

# Method to choose the banking option
def deposit_withdraw(choice):
    amount = 0
    if choice == '2':
        amount = input("How much do you want to deposit? ")
        deposit(amount)
    else: 
        amount = input("How much do you want to withdraw? ")
        withdraw(amount)

# This method deducts(withdraw) from the balance
def withdraw(amount):
    global balance
    if float(amount) > balance:
        print("Insufficient funds.")
        get_balance()
        return
    
    balance -= float(amount)
    get_balance()

# This method adds(deposits) to the balance
def deposit(amount):
    global balance
    balance += float(amount)
    get_balance()

# Main method
def main():
    print("Welcome to Fleeca Bank. How can we help you today?")
    print("--------------------------------------------------")
    while True:
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            get_balance()
        elif choice == '4':
            print("Thank you for banking with us.")
            break
        else:
            deposit_withdraw(choice)

        again =  input("Do you want to continue banking? y or n: ")
        if again == 'n':
            print("Thank you for banking with us.")
            break

main()