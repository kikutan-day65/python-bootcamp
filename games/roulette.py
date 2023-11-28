import random

name_list = []
roulette = True

while roulette:
    name = input("Enter the name who wanna join the roulette: ")
    name_list.append(name)
    again = input("You wanna add more? y/n: ").lower()
    if again == 'n':
        roulette = False
    else:
        continue

print("Joined: ", name_list)

chosen = random.choice(name_list)

print(f"congratulations! {chosen} is chosen")