# online delivery system 

username = "admin"
password = "1234"

print("======== ONLINE DELIVERY SYSTEM =========")

u = input("enter username:- ")
p = input("enter password:- ")

if u == username:
    if p == password:

        total_bill = 0
        orders = []

        while True:

            print("\n ---- MENU ----")
            print("1. pizza - rs 200")
            print("2. burger - rs 120")
            print("3 pasta - rs 180")
            print("4. exit")

            choice = int(input("select item:- "))

            if choice == 1:
                item = "pizza"
                price = 200
            elif choice == 2:
                item = "burger"
                price = 120
            elif choice == 3:
                item = "pasta"
                price = 180
            elif choice == 4:
                print("ordering completed")
                break
            else:
                print("invlaid choice")
                continue
            qty = int(input("enter quantity:- "))


            item_total = price * qty
            total_bill += item_total

            orders.append([item, qty, item_total])

            more = input("order more ? (yes/no): ")

            if more.lower() == "no":
                break

            print("\n === BILL DETAILS ====")

            for order in orders:
                print("item:", order[0])
                print("quantity:", order[1])
                print("amount:", order[2])
                print("-------------------")

            print("total bill =", total_bill)

            #NESTED CONDITION 

            if total_bill >= 1000:
                if total_bill >= 2000:
                    discount = total_bill * 0.20
                    print("20% discount applied")
                else:
                    discount = total_bill * 0.10
                    print("10% discount applied")
                
                final_amount = total_bill - discount
            else:
                final_amount = total_bill
            
            print("final amount = ", final_amount)

            #delivery charges

            if final_amount < 500:
                print("delivery charge = rs50")
                final_amount += 50
            else:
                print("free delivery")
        else:
            print("wrong password")
    else:
        print("wrong username")
