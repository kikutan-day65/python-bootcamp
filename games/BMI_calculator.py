while True:
    try:
        height = float(input("enter your height in m: "))
        weight = float(input("enter your weight in kg: "))
        break
    except ValueError as Verr:
        print("Plz enter the number: ", Verr)

BMI = weight / (height ** 2)

if BMI < 16.0:
    print("Underweight (Severe thinness)")
elif 16.0 <= BMI <= 16.9:
    print("Underweight (Moderate thinness)")
elif 17.0 <= BMI <= 18.4:
    print("Underweight (Mild thinness)")
elif 18.5 <= BMI <= 24.9:
    print("Normal range")
elif 25.0 <= BMI <= 29.9:
    print("Overweight (Pre-obese)")
elif 30.0 <= BMI <= 34.9:
    print("Obese (Class I)")
elif 35.0 <= BMI <= 39.9:
    print("Obese (Class II)")
elif BMI >= 40.0:
    print("Obese (Class III)")
else:
    print("something went wong")