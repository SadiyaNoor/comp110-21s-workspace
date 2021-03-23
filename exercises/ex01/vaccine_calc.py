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
tr_pr_v: int = int(input("Target percent vaccinated: "))

target_population: int = round(population * (tr_pr_v / 100))
unvaccinated: int = (target_population * 2) - Doses_administered
d_left: int = round(unvaccinated / Doses_per_day)

today: datetime = datetime.today()
calc_date: timedelta = timedelta(d_left)
N_date: datetime = today + calc_date

vac_op: str = str(tr_pr_v)
dlef_op: str = str(d_left)
str1op: str = "We will reach "
str2op: str = "% vaccination in "
str3op: str = " days which falls on "

print(str1op + vac_op + str2op + dlef_op + str3op + N_date.strftime("%B %d, %Y"))
