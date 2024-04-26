import random


def main():
    lvl = get_level()
    counter = 0

    for i in range (10):

        # Prepare info for a single problem
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        z = x + y

        # Ask for the user's answer for a single problem and check it - 3 attempts
        for j in range(3):
            ans = input(f"{x} + {y} = ")
            try:
                ans_i = int(ans)
            except ValueError:
                ans_i = -2
            finally:

                # If the answer is wrong, go to other attempts if any left
                if ans_i != z:
                    print("EEE")

                # If the answer is right, don't give any more attempts
                else:
                    counter += 1
                    break

        if ans_i != z:
            print(f"{x} + {y} = {z}")

    print(f"Score: {counter}")



def get_level():
    while True:
        try:
            l = int(input("Level: "))
        except ValueError:
            print("that must be an integer")
            pass
        else:
            if l == 1 or l == 2 or l == 3:
                return l


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    return random.randint(10 ** (level - 1), 10 ** level - 1)


if __name__ == "__main__":
    main()

