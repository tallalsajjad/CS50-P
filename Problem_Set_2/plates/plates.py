def main():
    Plate = input("Plates: ")
    if is_valid(Plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
     return (correct_length(s) and
             alphabet(s) and number(s) and
             zero(s))
def correct_length(s):

    return len(s) >= 2 and len(s) <=6
def alphabet(s):

    return s[:2].isalpha()

def number(s):
    return s.isalnum()
def zero(s):
     if any(char.isdigit() for char in s):
        first_digit = next(i for i, char in enumerate(s) if char.isdigit())
        if s[first_digit] == '0':
            return False
        return s[first_digit:].isdigit()
     return True

if __name__ == "__main__":
    main()

