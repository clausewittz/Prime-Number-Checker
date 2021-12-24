# Prime number is only divisible by 1 and itself.

# All numbers can be divided by 1. So we're gonna check if the number can be divided by itself.

def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
            print("Not a prime number.")
    
    if is_prime == True:
        print("Prime number!")

# If number % i == 0 then the number is not prime. Bcz prime number gives only 1 as a result. (Divided by itself)

n = int(input("Check this number: "))
prime_checker(number=n)
