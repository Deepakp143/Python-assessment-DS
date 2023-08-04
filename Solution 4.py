def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def get_number_of_days(year):
    if is_leap_year(year):
        return 366
    else:
        next_leap_year = year
        while True:
            next_leap_year += 1
            if is_leap_year(next_leap_year):
                break
        return (next_leap_year - year) * 365 + 1

def get_season(month, day):
    seasons = {
        (3, 20): "Spring",
        (6, 21): "Summer",
        (9, 22): "Fall",
        (12, 21): "Winter"
    }

    for key, value in seasons.items():
        if (month, day) < key:
            return value

    return "Winter"

def main():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))
    season = get_season(month, day)
    print("Season:", season)

    if is_leap_year(year):
        print(f"{year} is a leap year.")
        print("Number of days in the year:", get_number_of_days(year))
    else:
        next_leap_year = year
        while True:
            next_leap_year += 1
            if is_leap_year(next_leap_year):
                break
        print(f"{year} is not a leap year.")
        print("Next leap year:", next_leap_year)
        print("Number of days in the year:", get_number_of_days(year))
main()
