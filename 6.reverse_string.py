# Reverse string using two pointers
def reverse_string(string):
    
    if len(string) == 1:
        return string
    
    # Convert string to list
    chars = list(string)
    
    left = 0
    right = len(chars) - 1
    
    
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        right -= 1
        left += 1
        
    return "".join(chars)

string = input("Enter string: ")

reversed_string = reverse_string(string)
print(f"Reverse of {string}: {reversed_string}")


# Brute force
# a = ''
# for i in s:
#     a = i+a
    
# print(a)