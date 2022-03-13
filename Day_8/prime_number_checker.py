
def prime_number_check(number):
    is_prime=True
    for i in range(2,number-1):
        if number%i==0:
            is_prime=False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime")
number=int(input("Enter the number you want to check: "))
prime_number_check(number)