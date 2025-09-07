from datetime import date
import re
import sys
import inflect

class AgeInMinutes:
    def __init__(self, birth_date_str):
        self.birth_date_str = birth_date_str
        self.birth_date = self.parse_date(birth_date_str)
        self.current_date = date.today()
        self.age_in_minutes = self.calculate_age_in_minutes()
        self.age_in_words = self.convert_to_words(self.age_in_minutes)

    def parse_date(self, date_str):
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
            sys.exit("Invalid Date")
        year, month, day = map(int, date_str.split('-'))
        try:
            return date(year, month, day)
        except ValueError:
            sys.exit("Invalid Date")

    def calculate_age_in_minutes(self):
        delta = self.current_date - self.birth_date
        return delta.days * 24 * 60

    def convert_to_words(self, number):
        p = inflect.engine()
        return p.number_to_words(number, andword="")

    def get_age_in_words(self):
        return self.age_in_words

def main():
    birth_date_str = input("Date of birth: ")
    age_in_minutes = AgeInMinutes(birth_date_str)
    print(f"{age_in_minutes.get_age_in_words().capitalize()} minutes")

if __name__ == "__main__":
    main()
