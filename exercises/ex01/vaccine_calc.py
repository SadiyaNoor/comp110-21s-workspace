"""A vaccination calculator."""

__author__ = "730411656"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

population: int = int(input("Population: ")) 
Doses_administered: int = int(input("Doses administered: "))
Doses_per_day: int = int(input("Doses per day: "))
target_percent_vaccinated: int = int(input("Target percent vaccinated: "))

target_population: int = population * (target_percent_vaccinated / 100)
unvaccinated: int = (target_population * 2) - Doses_administered
days_left: float = unvaccinated / Doses_per_day

today: datetime = datetime.today()
calc_date: timedelta = timedelta(days_left)
reach_date: datetime = today + calc_date

print("We will reach " + str(target_percent_vaccinated) + "% in " + str(days_left) + " days, which falls on " + reach_date.strftime("%B %d, %Y"))
