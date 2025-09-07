import csv
import sys
output = []
def main():
    check()
    output = []
    try:
        with open(sys.argv[1], 'r') as csv_file_in:
            reader = csv.DictReader(csv_file_in)
            for row in reader:
                split_name = row["name"].split(",")
                output.append({'first': split_name[1].lstrip(), 'last': split_name[0], 'house': row['house']})

    except FileNotFoundError:
        sys.exit(f"Could not read,{sys.argv[1]}")

    with open(sys.argv[2], 'w') as csv_file_out:
        writer = csv.DictWriter(csv_file_out, fieldnames = ['first', 'last', 'house'])
        writer.writerow({"first": 'first', 'last': 'last', 'house': 'house'})
        print(writer)
        for row in output:
            writer.writerow({'first': row['first'], 'last': row['last'], 'house': row['house']})

def check():
    try:
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
            sys.exit("Not a CSV file")
    except IndexError:
        sys.exit("Too few command-line arguments")


if __name__ == "__main__":
    main()
