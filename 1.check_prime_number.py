# Program to check a number is prime/not prime

def is_prime(num):
    
    if num < 2:
        return False
    
    c = 2
    # # Only check divisors where c*c < num (i.e., up to √num)
    while(c*c < num):
        if num%c == 0:
            return False
        c += 1
    return True


num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
    

