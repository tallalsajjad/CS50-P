def main():
    Ask = input("Input: ")
    omitted = shorten(Ask)
    print(f"{omitted}")

def shorten(word):
    vowel = ['a', 'e', 'i', 'o', 'u']
    changes = ""
    for x in word:
        if x.lower() not in vowel:
            changes += x
    return changes

if __name__ == "__main__":
    main()
