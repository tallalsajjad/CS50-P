Fruits = {
    "apple": 130,
    "Avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapeps": 90,
    "honeydrew melon": 50,
    "Kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "Sweet Cherries": 100,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "Sweet Cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}

Name = input("Item: ")
for key in Fruits:
    if key in Name:

       print( "calories: ", Fruits[key])
