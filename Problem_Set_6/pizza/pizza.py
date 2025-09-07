import sys
import csv
import tabulate
def main():
    try:
        files = check()
        if not files.endswith("csv"):
            sys.exit("Not a CSV file")
        with open(files, 'r') as csv_file:
            file = csv.DictReader(csv_file)
            row = tabulate.tabulate(file, headers = "keys", tablefmt="grid")
            print(row)

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

if __name__ == "__main__":
    main()
