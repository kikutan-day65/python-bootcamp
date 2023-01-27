import random

coin = random.randint(0,1)

print("A coin is flipped")
guess = int(input("Guess heads(1) or tails(0): "))

if guess != 0 and guess != 1:
    print("plz enter heads(1) or tails(0)")
else:
    if guess == coin:
        print("You win")
    else:
        print("You lose")