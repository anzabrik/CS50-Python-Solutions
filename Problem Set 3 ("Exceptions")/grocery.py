groceries = {}
while True:
    try:
        item = input("")
    except EOFError:
        print()
        break
    else:
        item = item.upper()
        if item not in groceries:
            groceries[item] = 1
        else:
            groceries[item] += 1

for item, number in sorted(groceries.items()):
    print(number, item)



"""
dict(sorted(people.items()))
{1: 'Jill', 2: 'Jack', 3: 'Jim', 4: 'Jane'}

groceries = []


while True:
    one = {}
    try:
        item = input("Item: ")

    except EOFError:
        print()
        break
    else:
        item = item.upper()
        if item not in groceries:
            item_counter = 0
            one[item] = item_counter
            groceries.append(one)
        else:
            item_counter += 1
            one[item] = item_counter


for i in range(len(groceries)):
    print(groceries[i])

"""
