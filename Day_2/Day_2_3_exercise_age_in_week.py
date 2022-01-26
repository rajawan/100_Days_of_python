
#Get the current age from user
age=input("Enter your age: ")
#convert the age into int
age_as_int=int(age)
#calculate the remaining year, month, weeks and days
years=90 - age_as_int
days_remaining=round(years*365)
weeks_remaining=round( years*52)
months_remaining=round( years*12)
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
