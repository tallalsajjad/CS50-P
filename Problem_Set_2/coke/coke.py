cost = 50
Accepted =[25, 10, 5]

while cost > 0:

     insert = int(input("Insert coin: "))
     if insert in Accepted:
           cost -= insert
           if cost > 0:
               print(f"Amount due: {cost}")
           else:
                print(f"change owed: {-cost}")

     else:
         print(f"Amount due: {cost}")



