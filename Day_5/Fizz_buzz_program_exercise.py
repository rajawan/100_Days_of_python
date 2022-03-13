'''Making the best heard program fizzbuzz game
1.First need to print 1 to 100 using range function.
2.If any number divisable by 3 and 5 then print FizzBuzz instead of the number.
3.If any number divisable by 3 then print Fizz instead the number.
4.If any number divisable by 5 then print Buzz instead the number.

'''

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)