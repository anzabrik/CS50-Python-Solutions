from sys import argv, exit
from PIL import Image, ImageOps

if len(argv) < 3:
    exit("Too few command-line arguments")

elif len(argv) > 3:
    exit("Too many command-line arguments")

infilename_list = argv[1].split(".")
outfilename_list = argv[2].split(".")


if len(infilename_list) != 2:
    exit("The input file name does not end in .jpg, .jpeg, or .png")

if len(outfilename_list) != 2:
    exit("The output file name does not end in .jpg, .jpeg, or .png")

in_extension = infilename_list[1].lower()
out_extension = outfilename_list[1].lower()

if in_extension != "jpg" and in_extension != "jpeg" and in_extension != "png":
    exit("The input file name does not end in .jpg, .jpeg, or .png")

if out_extension != "jpg" and in_extension != "jpeg" and in_extension != "png":
    exit("The output file name does not end in .jpg, .jpeg, or .png")

if in_extension != out_extension:
    exit("The output and input files should have the same extension")

try:
    # Open infile
    person = Image.open(argv[1])

    # Open shirt and find out its size
    shirt = Image.open("shirt.png")
    shirt_s = shirt.size
    # Resize and crop person
    cropped_person = ImageOps.fit(person, shirt_s)
    # Overlay two pics
    cropped_person.paste(shirt,shirt)
    # Save result as output
    cropped_person.save(
        argv[2]
    )
except FileNotFoundError:
    exit("The file was not found")


