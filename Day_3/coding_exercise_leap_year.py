#calcualte if the given year is leap year or not
"""if a year is divisible by 4 and not divisible by 100 and
also not divisible by 400 then it would be a leap year"""
year=int(input("Which year do you want to check? "))
#check the year is leap or not
if year%4==0:
    if year%100==0:
        if year%400==0:
         print("The year is  a leap year")
        else:
            print("This is not a leap year")
    else:
        print("This year is a  leap yer")

else:
    print("This is not a leap year")