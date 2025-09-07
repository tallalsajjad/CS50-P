import inflect

def main():
    import sys
    names = []

    try:
        while True:
            name = input("Name:" )
            names.append(name)
    except EOFError:
        pass

    p = inflect.engine()
    farewell = p.join(names)
    print(f"Adieu, adieu, to {farewell}")

if __name__ == "__main__":
    main()
