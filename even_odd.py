while True:
    try:
        num = int(input("enter the integer number: "))
        break     
    except ValueError as Verr:
        print("plz enter the integer number: ", Verr)

if num % 2 == 0:
        print(f"{num} is even")
else:
    print(f"{num} is odd")