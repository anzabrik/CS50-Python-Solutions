answer = input("What's the answer to the Great Question of Life, the Universe and Everything? ")
answer = answer.lower()
answer = answer.strip()
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")