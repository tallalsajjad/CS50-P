def main():
    Text = input("Enter a text: ")
    print(Text)
    paragraph = convert(Text)
    print(paragraph)

def convert(emoticons):
    emoticons= emoticons.replace(":)", "🙂")
    emoticons= emoticons.replace(":(", "🙁")
    return emoticons

main()
