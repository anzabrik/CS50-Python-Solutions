import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Grab anything that is inside "" after src, if nothing - return None
    if match := re.search(r"src=\"(.+?)\"", s):
        original_url = match.group(1)
        return shorten(original_url)
    return None

# Grab everything that should stay, then concatenate these into a single string
def shorten(url):
    if matches := re.search(r"d/(.+)", url):
        return "https://youtu.be/" + matches.group(1)
    return None


if __name__ == "__main__":
    main()


