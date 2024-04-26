from validator_collection import validators, checkers, errors

def main():
    if (validate(input("Your email: "))):
        print("Valid")
    else:
        print("Invalid")

def validate(s):
    return checkers.is_email(s)


if __name__ == "__main__":
    main()