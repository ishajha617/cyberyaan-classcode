balance = 50000
pin = "1234"
attempt = 0

while attempt < 3:
    user_pin = input("enter atm pin:- ")

    if user_pin == pin:
        while True:

            print("\n ==== ATM MENU=====")
            print("1.check balance")
            print("2. deposit")
            print("3. withdraw")
            print("4. fund transfer")
            print("5. exit")

            choice = input("enter choice:- ")

            # check balance
            if choice == "1":
                print("current balance=", balance)
            #deposit
            elif choice == "2":
                amount = float(input("enter deposit amount: "))

                if  amount > 0:
                    balance += amount
                    print("deposit successful")
                    print("updated balance =", balance)
                else:
                    print("invalid amount")
            #withdraw
            elif choice == "3":
                amount = float(input("enter withdraw amount: "))

                if amount <= balance:
                    if  amount <= 20000:
                        balance -= amount
                        print("plaese collect cash")
                        print("remaining balance = ", balance)
                    else:
                        print("maximum withdrwal limit is 20000")
                else:
                    print("insufficient balance")

            #fund transfer
            elif choice == "4":
                account = input("enter beneficiary account number: ")
                if len(account) == 10:
                    amount = float(input("transfer amoubnt:- "))

                    if amount <= balance:
                        if amount <= 50000:
                            balance -= amount
                            print("transfer sucessfully")
                            print("transfered amount =", amount)
                            print("remaining balance =", balance)
                        else:
                            print("transfer limit exceeded")
                    else:
                        print("insufficient balance")
                else:
                    print("invalid account number")
                
            #exit
            elif  choice == "5":
                print("thanku you for banking with us")
                break
            else:
                print("invalid option")
            break
        else:
            attempt += 1
            print("wrong pin")
            print("remaining attempts =", 3 - attempt)

            if attempt == 3:
                print("atm card blocked")


