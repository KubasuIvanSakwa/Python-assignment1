salary = int(input("Enter your salary: \n"))
years = int(input("Enter your period of service: \n"))

if years >= 10:
    print("Net Salary: ksh.", salary+(salary*0.1))
elif years >= 6 and years <= 10:
    print("Net Salary: ksh.", salary+(salary*0.08))
elif years < 6:
    print("Net Salary: ksh.", salary+(salary*0.05))