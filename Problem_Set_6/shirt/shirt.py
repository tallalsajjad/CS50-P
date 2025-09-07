import sys
import os
from PIL import Image, ImageOps

NOTE = (".jpeg", ".png", ".jpg")

def main():
    check_arg()
    input_file = sys_argv_1()
    output_file = sys_argv_2()
    check_ext(input_file, output_file)

    try:
        with Image.open(input_file) as img:
            image_file = img.copy()
    except FileNotFoundError:
        sys.exit("Input file does not exist")

    shirt_file = Image.open("shirt.png")
    size = shirt_file.size
    mupuppet = ImageOps.fit(image_file, size)
    mupuppet.paste(shirt_file, (0, 0), shirt_file)
    mupuppet.save(output_file)

def check_arg():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line argument")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line argument")

def sys_argv_1():
    if not sys.argv[1].lower().endswith(NOTE):
        sys.exit("Invalid input")
    return sys.argv[1]

def sys_argv_2():
    if not sys.argv[2].lower().endswith(NOTE):
        sys.exit("Invalid output")
    return sys.argv[2]

def check_ext(input_file, output_file):
    ok_ext = [".jpg", ".jpeg", ".png"]
    ext1 = os.path.splitext(input_file)[1].lower()
    ext2 = os.path.splitext(output_file)[1].lower()
    if ext1 in ok_ext and ext2 in ok_ext:
        if ext1 != ext2:
            sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid file extensions")

if __name__ == "__main__":
    main()
