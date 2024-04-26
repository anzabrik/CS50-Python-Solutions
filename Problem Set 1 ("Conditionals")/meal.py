def main():
    ti = input("What time is it? ")
    t = convert(ti)
    meal = ""
    if t >= 7 and t <= 8:
        meal = "breakfast"
        print(f"{meal} time")
    if t >= 12 and t <= 13:
        meal = "lunch"
        print(f"{meal} time")
    if t >= 18 and t <= 19:
        meal = "dinner"
        print(f"{meal} time")



def convert(time):
    hours, minutes = time.split(":")
    h = int(hours)
    min = int(minutes)
    min_into_decimal = round((min / 60), 2)
    return h + min_into_decimal






if __name__ == "__main__":
    main()