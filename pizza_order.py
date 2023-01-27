total = 0

size = input("what size pizza do u want? S, M, or L: ").upper()

if size == 'S':
    total += 15
elif size == 'M':
    total += 20
elif size == 'L':
    total += 25
else:
    print("enter only S, M, or L")

add_peeperoni = input("do u wanna add pepperoni? Y or N: ").upper()

if add_peeperoni == 'Y':
    total += 3
else:
    print("enter only Y/N")

add_cheese = input("do u wanna add extra cheese? Y or N: ").upper()

if add_cheese == 'Y':
    total += 1
else:
    print("enter only Y/N")


print(f"total bill is ${total}")
print("thank you")
