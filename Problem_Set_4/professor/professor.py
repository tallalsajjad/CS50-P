import random

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                continue
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        for attempts in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")

            if attempts == 2:
                print(f"The correct answer was {correct_answer}.")

    print(f"Score: {score}")

if __name__ == "__main__":
    main()
