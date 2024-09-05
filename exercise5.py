# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    selected_month = input('Enter the month of the year (JAN - DEC): ').upper()
    day = input('Enter a day of the month (1-31): ')
    if not day.isdigit() or selected_month not in months:
        print('Please enter a valid month and day.')
        return
    day = int(day)
    if day < 1 or day > 32:
        print('input must be between 1 and 31')
        return
    if selected_month == 'DEC' and day >= 21 or selected_month in ['JAN', 'FEB'] or (selected_month == 'MAR' and day <= 19):
            season = 'Winter'
            print(f'{selected_month.capitalize()} {day} is in {season}.')
    elif (selected_month == 'MAR' and day >= 20) or selected_month in ['APR', 'MAY'] or (selected_month == 'JUN' and day <= 20):
            season = 'Spring'
            print(f'{selected_month.capitalize()} {day} is in {season}.')
    elif (selected_month == 'JUN' and day >= 21) or selected_month in ['JUL', 'AUG'] or (selected_month == 'SEP' and day <= 21):
            season = 'Summer'
            print(f'{selected_month.capitalize()} {day} is in {season}.')
    elif (selected_month == 'SEP' and day >= 22) or selected_month in ['OCT', 'NOV'] or (selected_month == 'DEC' and day <= 20):
            season = 'Fall'
            print(f'{selected_month.capitalize()} {day} is in {season}.')

# Call the function
determine_season()
