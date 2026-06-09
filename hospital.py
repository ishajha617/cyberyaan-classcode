print(" ===== hospital managemnet system =====")

patients = []

while True:
    print("\n1. new patient")
    print("2. exit")

    choice = int(input("enter choice:- "))

    if choice == 1:
        name = input("enter patient name:- ")
        age = int(input("enter your age:- "))

        print("\nAVAILABLE DOCTORS")
        print("1. general physician (500)")
        print("2. cardiologist (1000)")
        print("3. orthopedic (800)")

        doctor_choice = int(input("selerct doctor:- "))

        if doctor_choice == 1:
            doctor = "general physician"
            doctor_fee = 500
        
        elif doctor_choice == 2:
            doctor = "cardiologist"
            doctor_fee = 1000
        elif doctor_choice == 3:
            doctor = "orthepedic"
            doctor_fee = 800
        else:
            print("invalid doctor")
            continue
        print("\n Room type")
        print("1. general ward (1000/day)")
        print("2. private room (3000/day)")
        print("3. icu (7000/day)")

        room_choice = int(input("select room :- "))

        days = int(input("number of days:- "))

        if room_choice == 1:
            room = "general ward"
            room_charge = 1000 * days

        elif room_choice == 2:
            room = "private room"
            room_charge = 3000 * days
        elif room_choice == 3:
            room = "icu"
            room_charge = 7000 * days
        else:
            print("invalid room")
            continue
        madicine_charge = int(input("enter madicine charge:- "))
        total_bill = doctor_fee + room_charge + madicine_charge

        #nested condition 

        if age >= 60:
            if total_bill >= 10000:
                discount = total_bill * 0.20
            else:
                discount = total_bill * 0.10

        else:

            if total_bill >= 20000:
                discount = total_bill * 0.15
            else:
                discount = 0
        final_bill = total_bill - discount

        patients.append([
            name,
            age,
            doctor,
            room,
            days, 
            madicine_charge,
            final_bill
        ])
        print("\n patient added successfully")

    elif  choice == 2:
        break
    else:
        print("invalid choice")
print("\n ===== hospital report =======")

for patient in patients:

    print("\n --------------------------")
    print("patient name :- ", patient[0])
    print("age:- ", patient[1])
    print("doctor :- ", patient[2])
    print("room type :- ", patient[3])
    print("days:- ", patient[4])
    print("madicine fee :- ", patient[5])
    print("final bill :- ", patient[6])

print("\n total patients registered :- ", len(patients))
print("thank you for using hospital management")