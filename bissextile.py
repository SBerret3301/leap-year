# Function to check if a given year is a leap year
def is_leap_year(year):
    # Leap year conditions:
    # 1. Divisible by 4
    # 2. Not divisible by 100 unless also divisible by 400
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

# Function to find leap years in a given century
def leap_year(century):
    years = []  # List to store leap years
    for i in range((century - 1) * 100, century * 100):
        if is_leap_year(i):  # Check if the current year is a leap year
            years.append(i)  # Add the leap year to the list
    return years

# Get input from the user for the century
century = int(input("Enter a century: "))
# Display the leap years of the specified century
print("The leap years of the century", century, "are:", leap_year(century))



