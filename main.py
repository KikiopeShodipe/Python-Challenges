import random
n = random.randint(1,100)
while True:
    g = int(input("Guess the number: "))
    if g < n:
        print("Too low!")
    elif g > n:
        print("Too high!")
    else:
        print("Corrent!")
        break