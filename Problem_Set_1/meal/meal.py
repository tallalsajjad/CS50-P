def main():
    meal = input("What time is it? ")
    Answer = convert(meal)
    if 7<= Answer <=8:
         print("breakfast time")
    elif 12<= Answer <=13:
         print("lunch time")
    elif 18<= Answer <=19:
         print("dinner time")



def convert(time):
    Period = time.split(":")
    hours = int(Period[0])
    minutes = int(Period[1])

    return hours + minutes/60





if __name__ == "__main__":
    main()
