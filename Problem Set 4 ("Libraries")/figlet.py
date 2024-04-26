from pyfiglet import Figlet
from sys import argv, exit

figlet = Figlet()

if len(argv) != 1 and len(argv) != 3:
    exit("Usage: provide zero or no cmdline arguments")

if len(argv) == 3:
    if argv[1] != "-f" and argv[1] != "--font":
        exit("Usage: -f name_of_the_font")
    if argv[2] not in figlet.getFonts():
            exit("Usage: -f name_of_the_font")
    figlet.setFont(font=argv[2])

inp = input("Input: ")

print(figlet.renderText(inp))



