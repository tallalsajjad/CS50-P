def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
     return (correct_length(s) and
             alphabet(s) and number(s) and
             zero(s))
def correct_length(s):

    if len(s) >= 2 and len(s) <=6:
        return True
def alphabet(s):
    if s[:2].isalpha():
        return True

def number(s):
    if s.isalnum():
        return True
def zero(s):
     if any(char.isdigit() for char in s):
        first_digit = next(i for i, char in enumerate(s) if char.isdigit())
        if s[first_digit] == '0':
            return False
        return s[first_digit:].isdigit()

     return True



main()
