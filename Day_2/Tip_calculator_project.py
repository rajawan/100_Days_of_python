

#Write your code below this line 👇
print("Welcome to the tip calculator")
#Get the total bill amount
bill= float(input("What was the total bill? "))
#Get the discount amount
tip_amount=int(input("What perchantage tip would you like to give? 10, 12, or 15? "))
final_tip=tip_amount/100
#Get the total number of people
number_of_people=int(input("How many people to split the bill? "))
#calculate the result
final_result=round((final_tip*bill+bill))
print(final_result)