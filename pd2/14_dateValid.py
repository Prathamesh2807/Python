# Enter following data to Check if a given date is valid.
day = 29
month = 2
year = 2024

# Initialize variables
is_year_valid = "invalid"
is_month_valid = "invalid"
is_day_valid = "invalid"

# Check if year is valid
if year > 0 and year < 10000:
    is_year_valid = "valid"

# Check if year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    is_year_leap = "leap"
else:
    is_year_leap = "not a leap"

# Check if month is valid
if month > 0 and month < 13:
    is_month_valid = "valid"

# Check if day is valid
if month == 2:  # February
    if is_year_leap == "leap":
        if day > 0 and day <= 29:
            is_day_valid = "valid"
    else:  # Not a leap year
        if day > 0 and day <= 28:
            is_day_valid = "valid"
elif month in [1, 3, 5, 7, 8, 10, 12]:  # Months with 31 days
    if day > 0 and day <= 31:
        is_day_valid = "valid"
elif month in [4, 6, 9, 11]:  # Months with 30 days
    if day > 0 and day <= 30:
        is_day_valid = "valid"

# Check if the date is valid
if is_day_valid == "valid" and is_month_valid == "valid" and is_year_valid == "valid":
    print(f"The date {day}/{month}/{year} is valid.")

else:
    print(f"The date {day}/{month}/{year} is not valid.")