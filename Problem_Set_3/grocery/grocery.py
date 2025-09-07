List = {}

while True:
    try:
        item = input().lower()
        List[item] = List.get(item,0)+1
    except EOFError:
        print()
        for item in sorted(List.keys()):
            print(List[item], item.upper())
        break


