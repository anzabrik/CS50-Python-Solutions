months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

month = -1
day = -1
year = -1

while month < 0 or month > 12 or day < 0 or day > 31 or year < 0 or year > 9999:
    input_date = input("Input date: ")

    # Identify the format of the input
    if len(input_date) > 10: # if the input contains the name of the month
        # Split input
        date_list_w = input_date.split()
        if date_list_w[0] in months:
            month = months.index(date_list_w[0]) + 1
        try:
            if date_list_w[1][-1] == ",":
                day = int(date_list_w[1].strip(","))
            year = int(date_list_w[2])
        except (ValueError, IndexError):
            pass


    else: # if the input is like 9/8/1636
        date_list_i = input_date.split("/")
        try:
            month = int(date_list_i[0])
            day = int(date_list_i[1])
            year = int(date_list_i[2])
        except (ValueError, IndexError):
            pass

print(f"{year}-{month:02}-{day:02}")






"""

month-day-year order, formatted like 9/8/1636 or September 8, 1636,
wherein the month in the latter might be any of the values in the list below

Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format,
prompt the user again. Assume that every month has no more than 31 days; no need to validate whether
a month has 28, 29, 30, or 31 days.
"""