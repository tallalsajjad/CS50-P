import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
f = figlet.getFonts()

if len(sys.argv) == 1:

    font = random.choice(f)
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):

    if sys.argv[2] in f:
        font = sys.argv[2]
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

figlet.setFont(font=font)
command = input("Input text: ")
print(figlet.renderText(command))
