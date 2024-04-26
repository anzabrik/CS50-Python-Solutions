import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Extract all the ums
    matches_list = re.findall(r"\bum\b", s, re.IGNORECASE)

    # Count lenth of matches_list
    return len(matches_list)


if __name__ == "__main__":
    main()

