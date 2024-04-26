from datetime import date
import sys
import re
import inflect


def main():

    born_str = input("Your date of birth, YYYY-MM-DD: ")
    print(get_age(born_str))


def get_age(born_str):

    today = date.today()
    # If input is valid, transform the string into date object
    if match := re.match(r"[1-2][90]\d\d-\d\d?-\d\d?", born_str):
        year_s, month_s, day_s = born_str.split("-")
        year = int(year_s)
        month = int(month_s)
        day = int(day_s)
        born_date = date(year, month, day)

        # Find the difference in days
        age_days = today - born_date

        # Transform difference into minutes
        age_minutes = age_days.days * 24 * 60

        # Transform into words
        p = inflect.engine()
        age = p.number_to_words(age_minutes, andword="").capitalize()
        return f"{age} minutes"



    else:
        sys.exit("Date format: YYYY-MM-DD")



if __name__ == "__main__":
    main()