age = int(input("enter your age :- "))
salary = int(input("enter your salary:- "))
credit_score = int(input("enter your credit score:- "))

if age >= 18:
    print("age verfication passed")
    if salary >= 30000:
        print("salary verfication done")
        if credit_score >= 700:
            print("loan approved")
        else:
            print("loan rejected")
            print("reason low credit score")
    else:
        print("loan rejected")
        print("reason insifficient salary")
else:
    print("loan reject")
    print("reason age below 18")
