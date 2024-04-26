def main():
    s = input()
    result = convert(s)
    print(result)

def convert(some_string):
    some_string = some_string.replace(":)", "🙂")

    some_string = some_string.replace(":(", "🙁")
    return some_string

if __name__ == "__main__":
    main()