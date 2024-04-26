"""
 Format the table using the library’s grid forma
"""

import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if sys.argv[1][-4:] != ".csv":
    sys.exit("Provide the name of a python file, which ends in '.csv'")

menu_list = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            menu_list.append(row)

except FileNotFoundError:
    sys.exit("File doesn't exist")

print(tabulate(menu_list, headers="keys", tablefmt="grid"))
