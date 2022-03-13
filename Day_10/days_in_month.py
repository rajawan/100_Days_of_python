def is_leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def days_in_month(year,month):
    months_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap_year(year) and month==2:
        return f"{29} Days this month"
    return f"{months_days[month]} Days this month"
year=int(input("Enter a year: "))
month=int(input("Enter a month: "))
days=days_in_month(year,month)
print(days)