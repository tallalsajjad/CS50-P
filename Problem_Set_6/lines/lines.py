import sys
def main():
    try:
        files = check()
        if not files.endswith("py"):
            sys.exit("Not a Python file")
        with open(files, 'r') as file:
            lines = file.readlines()
            count = 0
            for line in lines:
                if check_comment_space(line) == False:
                    count += 1
            print(count)

    except FileNotFoundError:
        sys.exit("File does not exist")

def check():
    try:
        if sys.argv[2:]:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1]:
            return sys.argv[1]
    except IndexError:
        sys.exit("Too few command-line arguments")

def check_comment_space(line):
    if line.isspace():
        return True
    if line.strip().startswith('#'):
        return True
    return False

if __name__ == "__main__":
    main()
