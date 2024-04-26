import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
    except EOFError:
        print()
        break
    else:
        names.append(name)

mylist = p.join(names)
print("Adieu, adieu, to", mylist)

