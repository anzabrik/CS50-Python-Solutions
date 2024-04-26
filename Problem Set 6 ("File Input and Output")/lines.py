import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if sys.argv[1][-3:] != ".py":
    sys.exit("Provide the name of a python file, which ends in '.py'")

counter = 0

try:
    with open(sys.argv[1]) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            # The row doesn't contain only " "
            if line:
                # Does the row start with "#" or " #"
                if line[0] != "#":
                    counter += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(counter)

