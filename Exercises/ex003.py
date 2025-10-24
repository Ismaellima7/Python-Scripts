""" Create a Python script that reads the day, month, and year of a person's birth and displays a message with the formatted date. """

day = int(input('Day: '))
month = str(input('Month: ')).title()
birth = int(input('Birth: '))

print(f'You were born on {day} of {month} of {birth}. Is this correct?')