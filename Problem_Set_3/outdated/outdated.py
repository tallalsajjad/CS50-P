months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def parse_date(date_str):
    # Try to parse date in numeric format (e.g., 9/8/1636)
    try:
        month, day, year = date_str.strip().split('/')
        month = int(month)
        day = int(day)
        year = int(year)
        if 1 <= month <= 12 and 1 <= day <= 31:
            return f"{year:04}-{month:02}-{day:02}"
    except ValueError:
        pass

    # Try to parse date in textual format (e.g., September 8, 1636)
    try:
        month_day, year = date_str.strip().split(',')
        month_name, day = month_day.split()
        month = months.index(month_name) + 1
        day = int(day)
        year = int(year.strip())
        if 1 <= day <= 31:
            return f"{year:04}-{month:02}-{day:02}"
    except (ValueError, IndexError):
        pass

    return None

def main():
    while True:
        date_str = input("Enter a date (e.g., 9/8/1636 or September 8, 1636): ")
        formatted_date = parse_date(date_str)
        if formatted_date:
            print(formatted_date)
            break
        else:
            print("Invalid date format. Please try again.")

if __name__ == "__main__":
    main()