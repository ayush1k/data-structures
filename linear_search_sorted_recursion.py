def recursive_linear_search(arr,x,i):
    if i >= len(arr):
        return -1
        
    if arr[i] > x:
        return -1
        
    if arr[i] == x:
        return i
        
    
    return recursive_linear_search(arr,x,i+1)
    

my_sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_to_find = 100

result = recursive_linear_search(my_sorted_array, target_to_find, i=0)
if result == -1:
    print("Element not present")
else:
    print("element present at", result)