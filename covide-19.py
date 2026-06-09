print("======= COVID-19 REGISTRATION SYSTEM=========")

name = input("enter patient name:- ")
age = input("enter age:- ")
city = input("enter city:- ")

temperature = float(input("enter body temperature(c):- "))
oxygen = int(input("enter oxygen level(%) :- "))

fever = input("fever (yes/no): ").lower()
cough = input("cough (yes/no) : ").lower()

breathing = input("breathing problem (yes/no): ").lower()

print("\n ======= report =========")

# age verfication 

if age <= "18" :
    print("registration rejected")
    print("reason patient must be 18 year or older")

#location verfication '
elif city.lower() != "delhi":
    print("registration rejected")
    print("reason only delhi person to allow ")
else:
    print("sucessfully done allow to registration")
    print(f"my name is {name} pratihast ")
    print("age:", age)
    print("city:", city)


    #HIGH RISK CONDITION 
    if oxygen < 90 :
        print("\nstatus: critical")
        print("icu admission urgent")
    elif temperature >= 102  and breathing == "yes":
        print("\n status high risk")
        print("hospital addmisson urgent")
    elif fever == "yes" and cough == "yes":
        print("\n status moderate")
    elif fever == "yes":
        print("\n status low risk")
    else:
        print("\nstatus healthy")
        print("no major")
print("thanku for visit our side")
print("go other place and con")

