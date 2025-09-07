import random

def positive_no(level):
    while True:
        try:
            values = input(level)
            values = int(values)
            if values > 0:
                return values
        except ValueError:
            pass

def main():
    check = positive_no("Level: ")
    target = random.randint(1, check)

    while True:
        guess = positive_no("Guess: ")
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
