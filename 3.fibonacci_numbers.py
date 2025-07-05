# Program to print Fibonacci numbers
# Output: 0, 1, 1, 2, 3, 5, 8, 13, ...

def fibonacci_num(num):
    start = 0
    end = 1

    print(start)
    if num > 1:
        print(end)

    for i in range(2, num):
        result = start + end
        print(result)
        start = end
        end = result

# Input from user
num = int(input("Enter the number of Fibonacci terms: "))
fibonacci_num(num)
