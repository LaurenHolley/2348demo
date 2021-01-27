# Lauren Holley
# 1861058
print("Birthday Calculator")
print("Current Day")
c_month = int(input("Enter the current month number"))
c_day = int(input("Enter the current day"))
c_year = int(input("Enter the current year"))
print("Month: ", c_month)
print("Day: ", c_day)
print("Year: ", c_year)
print("Birthday")
bd_month = int(input("Enter your birth month"))
bd_day = int(input("Enter your birth day"))
bd_year = int(input("Enter your birth year"))
print("Month: ", bd_month)
print("Day: ", bd_day)
print("Year: ", bd_year)
if bd_month == c_month and bd_day == c_day:
    print("Happy Birthday!")
age_years = c_year - bd_year
if c_month >= bd_month:
    if c_day >= bd_day:
        print("You are", age_years, "years old.")
    else:
        print("You are", age_years - 1, "years old.")
else:
        print("You are", age_years - 1, "years old")

