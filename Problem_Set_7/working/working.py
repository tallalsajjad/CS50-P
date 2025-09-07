import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.search(r'^(([0-9][0-2]*):*([0-5][0-9])* ([A_P]M)) to (([0-9][0-2]*):*([0-5][0-9])* ([A_P]M))$', s)
    if match:
        pieces = match.groups()

        if int(pieces[1]) > 12 and int(pieces[5]) > 12:
            return ValueError
        first_time = change_format(pieces[1], pieces[2], pieces[3])
        second_time = change_format(pieces[5], pieces[6], pieces[7])
        return first_time + ' to ' + second_time
    else:
        raise ValueError

def change_format(hour, minute, am_pm):
    if am_pm == 'PM':
        if int(hour) == 12:
            new_h = 12
        else:
            new_h = int(hour) + 12
    else:
        if int(hour) == 12:
            new_h = 0
        else:
            new_h = int(hour)
    if minute == None:
        new_m = ':00'
        new_time = f"{new_h:02}" + new_m
    else:
        new_time = f"{new_h:02}" + ":" + minute
    return new_time

if __name__ == "__main__":
    main()

