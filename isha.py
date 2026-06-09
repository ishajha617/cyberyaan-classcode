balance = 10000

pin = int(input("enter pin:- "))

if pin == 1234:
    print("\nlogin sucessful")

    print("""
        1. check balance 
        2. deposit
        3. withdraw
          """)
    
    choice = int(input("choose option:- "))
    if choice == 1:
        print("current balance:- ", balance)
    elif choice == 2:
        amount = int(input("enter deposit amount:- "))
        balance += amount

        print("deposit successful")
        print("new balance:- ", balance)
    elif choice == 3 :
        amount = int(input("enter withdraw amount:- "))

        if amount <= balance:
            balance -= amount
            print("withdrawal sucessfull")
            print("reamaining balance :", balance)
        else:
            print("balance problem")
    else:
        print("invalid option")
else:
    print("invalid pin")
                 