"""
convert expects a str in X/Y format as input, wherein each of X and Y is an integer,
and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive.
If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError.
If Y is 0, then convert should raise a ZeroDivisionError.

gauge expects an int and returns a str that is:
"E" if that int is less than or equal to 1,
"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.
"""
def main():
    fr = input("Write here: ")
    fr_into_percentage = convert(fr)

    s = gauge(fr_into_percentage)
    print(s)


def convert(fraction):
    while True:
        slash_index = fraction.find("/")
        try:
            x = float(fraction[:slash_index])
            y = float(fraction[(slash_index + 1):])
            if x > y:
                raise ValueError("X must be smaller than Y")
            elif y == 0:
                raise ZeroDivisionError("You can't divide to zero")
            elif x.is_integer() and y.is_integer():
                x = int(x)
                y = int(y)
                return round(x / y * 100)
            else:
                raise ValueError("X must be smaller than Y")

        except (ValueError, ZeroDivisionError):
            fraction = input("Write here: ")



def gauge(percentage):
    if percentage <= 1:
       return "E"
    elif percentage >= 99:
       return "F"
    else:
       return f"{percentage}%"


if __name__ == "__main__":
    main()