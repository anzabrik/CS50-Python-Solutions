vowels = "AEIOUaeiou"
message = input("Your message: ")
for letter in message:
    if letter not in vowels:
        print(letter, end="")
print()