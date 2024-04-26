import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if sys.argv[1][-4:] != ".csv":
    sys.exit("Provide the name of a file which ends with '.csv'")

students = []

try:
    with open(sys.argv[1]) as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            students.append(row)

except FileNotFoundError:
    sys.exit("File doesn't exist")

for student in students:
    last, first = student["name"].split(", ")
    student.pop("name")
    student["first"] = first
    student["last"] = last

with open(sys.argv[2], "w") as outfile:
    outfile_writer = csv.DictWriter(outfile, fieldnames = ["first", "last", "house"])
    outfile_writer.writeheader()
    for student in students:
        outfile_writer.writerow(student)

