while True:
    try:
        age = int(input("What is your current age?: "))
        break
    except ValueError as Verr:
        print("plz enter the integer number: ", Verr)

years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left")