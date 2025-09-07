from validator_collection import validators

def main():
    Ask = input("what's your email address? ")
    output = validate(Ask)
    print(output)

def validate(v):
    try:
        validators.email(v)
        return "Valid"
    except:
        return "Invalid"


if __name__ == "__main__":
    main()
