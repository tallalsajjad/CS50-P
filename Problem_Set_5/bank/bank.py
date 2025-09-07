def main():
    Money = input("Greeting: ")
    winner = value(Money)
    print(f"${winner}")

def value(greeting):
    Hello = greeting.strip().lower()
    if Hello == "hello":
        return 0
    elif Hello.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
