# program to  list the prime numbers
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

num = int(input("Number of prime numbers: "))

for i in range(num):
    print(f"{i}:{is_prime(i)}")