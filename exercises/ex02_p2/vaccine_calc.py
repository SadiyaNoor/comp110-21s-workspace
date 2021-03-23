"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730411656"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    str1: str = " days, which falls on "
    # TODO 2: Call days_to_target and store result in a variable.
    days_till: int = days_to_target(population, doses, doses_per_day, target)
    # TODO 4: Call future_date and store result in a variable.
    ft_d8out: str = future_date(days_till)
    # TODO 5: Print the expected output using the variables above.
    print("We will reach " + str(target) + "%" + " vaccination in " + str(days_till) + str1 + ft_d8out)


# TODO 1: Define days_to_target function
def days_to_target(a: int, b: int, c: int, d: int) -> int:
    """This is to find the days remaining till target is reached."""
    target_population: int = round(a * (d / 100))
    unvaccinated: int = (target_population * 2) - b
    d_left: int = round(unvaccinated / c)
    return(d_left)


# TODO 3: Define future_date function
def future_date(days_till: int) -> str: 
    """To find the date target reached."""
    today: datetime = datetime.today()
    calc_date: timedelta = timedelta(days_till)
    N_date: datetime = today + calc_date
    return(N_date.strftime("%B %d, %Y"))


if __name__ == "__main__":
    main()
