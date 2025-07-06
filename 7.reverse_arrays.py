# Reverse array using two pointers
def reverse_arr(arr):
    
    new_arr = arr[:] #Create a shallow copy
    if len(new_arr) == 1:
        return new_arr
    
    
    left = 0
    right = len(new_arr) - 1
    
    
    while left < right:
        new_arr[left], new_arr[right] = new_arr[right], new_arr[left]
        right -= 1
        left += 1
        
    return new_arr

num_elements = int(input("Enter number of elements: "))
arr = []
for i in range(num_elements):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)
    
reversed_arr = reverse_arr(arr)

print(f"Reversed array of {arr}: {reversed_arr}")
