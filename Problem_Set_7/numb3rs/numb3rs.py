import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        digits = ip.split(".")
        for digit in digits:
            if int(digit) > 255 or int(digit) < 0:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
