def recursive_linear_search(arr,x,i):
    # Base Case 1: If we've searched the whole array, the target isn't there.
    if i >= len(arr):
        return -1
        
    # Base Case 2 (Optimization): If the current item is larger than the target,
    # we can stop because the array is sorted. The target cannot be found.
    if arr[i] > x:
        return -1
        
    # Base Case 3: We found the target at the current index.
    if arr[i] == x:
        return i
        
    # Recursive Step: If none of the base cases are met,
    # call the function again to check the next index
    return recursive_linear_search(arr,x,i+1)
    

my_sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_to_find = 100

result = recursive_linear_search(my_sorted_array, target_to_find, i=0)
if result == -1:
    print("Element not present")
else:
    print("element present at", result)