def linear_search(arr, target, i=0):
    
    if i >= len(arr):
        return -1
    
    if arr[i] == target:
        return i
    
    return linear_search(arr, target, i+1)

my_sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_to_find = 72

result = linear_search(my_sorted_array, target_to_find, i=0)
if result == -1:
    print("Element not present")
else:
    print("element present at", result,"if we start counting from 0")