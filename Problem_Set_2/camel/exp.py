cost = 50
Accepted =[25, 10, 5]

while cost > 0:
    print(f"Amount due: {cost} cents")
    insert = int(input("Insert coin: "))

    if insert in Accepted:
         cost -= insert
    else:
        print("Insert in range 25 10 5")

change = 0 if cost >=0 else -cost
print(f"change owned: {change} cents")

