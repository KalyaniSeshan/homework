# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list

import random

days = 365

people = 23
shared = 0
trials = 10000

for n in range(trials):
	birthdays = []
	for i in range(people):
		birthday = random.randint(1, days)
		if birthday in birthdays:
			shared += 1
			break
		else: birthdays.append(birthday)
print(shared / trials)

"""
python3 33birthday.py 365 23
0.571
"""

