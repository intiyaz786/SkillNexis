"""Mini Project (W1):
“Simple ATM Simulator”
● User login (PIN-based)
● Options: check balance, deposit, withdraw
● Use functions for each operation"""
def check_balance(balance):
    print("Current balance: ",balance)
def deposit(balance):
    amount=float(input("Enter the deposit amount: "))
    balance+=amount
    print("Amount Deposited Successfully")
    return balance
def withdraw(balance):
    amount=float(input("Enter the withdrawal amount: "))
    if amount<=balance:
        balance-=amount
        print("Please collect the cash")
    else:
        print("Insufficient balance")
    return balance
def atm():
    balance=10000
    while True:
        print("\n----ATM MENU---")
        print("1.Check Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.EXit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            check_balance(balance)
        elif choice==2:
            balance=deposit(balance)
        elif choice==3:
            balance=withdraw(balance)
        elif choice==4:
            print("Thank you for using ATM")
            break
        else:
            print("Invalid Choice")
atm()