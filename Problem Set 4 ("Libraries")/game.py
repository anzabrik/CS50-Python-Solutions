import random


while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

number = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess > 0:
            if guess == number:
                print("Just right!")
                break
            elif guess < number:
                print("Too small!")
            else:
                print("Too large!")
