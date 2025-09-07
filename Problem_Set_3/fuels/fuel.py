def main():
    while True:
        ask = input("Fraction: ")
        try:
            hello = convert(ask)
            break
        except (ValueError, ZeroDivisionError):
            continue

    if hello  <= 1:
        print("E")
    elif hello  >= 99:
        print("F")
    else:
        print(f"{hello}%")

def convert(ask):
    x, y = ask.split('/')
    x = int(x)
    y = int(y)

    if x > y or y == 0:
        raise ValueError("Invalid fraction")

    return round((x / y) * 100)

if __name__ == "__main__":
    main()
