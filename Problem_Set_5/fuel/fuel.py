def main():
    ask = input("Fraction: ")
    try:
        fraction_to_number = convert(ask)
        answer = gauge(fraction_to_number)
        print(f"{answer}")
    except (ValueError, ZeroDivisionError) as e:
        print(e)

def convert(ask):
    try:
        x, y = ask.split('/')
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError("Division by zero")
        if x > y:
            raise ValueError("Invalid input")
        f = x / y
        p = round(f * 100)
        return p
    except ValueError:
        raise ValueError("Invalid input")

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
