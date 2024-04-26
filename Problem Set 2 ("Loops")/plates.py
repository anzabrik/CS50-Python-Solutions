def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[:2].isalpha() and len(s) <= 6 and len(s) >= 2 and s.isalnum():
        if s.isalpha():
            return True
        for i in range(len(s)):
            if s[i].isnumeric():
                if s[i] != "0":
                    return s[i:].isnumeric()
                else:
                    return False
    return False


if __name__ == "__main__":
    main()



