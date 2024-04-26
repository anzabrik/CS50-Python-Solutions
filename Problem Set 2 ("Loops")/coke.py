d = 50
c = 0
def main():
    return change(d, c)


def change(due, coin):
    if due <= 0:
        chng = due * -1
        print(f"Change Owed: {chng}")
        return

    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        due -= coin
    return change(due, coin)


if __name__ == "__main__":
    main()