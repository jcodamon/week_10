#Jesse Codamon, Esteban Alvarez, Cesar Guzman
#Question 7
energy_usage = int(input("What is your total energy usage in kilowatt-hours?: "))
low_income = input("Are you a registered low-income household? (Y or N):")

if energy_usage < 200:
    if low_income == "Y": #is low income
        print("Discounted rate of $0.08/kWh applies.")
    else: #is not low income
        print("Standard rate of $0.10/kWh applies.")
if energy_usage >= 200 and energy_usage <= 500: #energy usage is more than or equal to 200 and less than or equal to 500
    print("Medium usage rate of $0.12/kWh applies.")
if energy_usage > 500: #energy usage is over 500
    if low_income == "Y": #is low income
        print("Discounted high usage rate of $0.15/kWh applies.")
    else: #is not low income
        print("High usage rate of $0.20/kWh applies.")

#Question 8
student = input("Are you a student? (Y or N): ")
age = int(input("What is your age?: "))
local = input("Are you a local resident?: (Y or N): ")

if student == "Y":
    if age < 18: #if student is under 18
        print("Eligible for free student membership.")
    if age >= 18: #if student is over or equal to 18
        if local == "Y": #student is local
            print("Eligible for discounted student membership.")
        else: #student is not local
            print("Nothing.")

if student == "N": #not a student
    if age > 65: #over 65
        if local == "Y": #is local
            print("Eligible for senior resident membership.")
        else: #is not local
            print("Standard membership rates apply.")
   
