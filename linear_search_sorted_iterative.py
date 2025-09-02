def linear_search(arr,x):
    # Loop through the array from the first index (0) to the last one.
    for i in range(len(arr)):
        # If the item at the current index matches the target...
        if arr[i]==x:
            # ...return the index immediately.
            return i
        
    # If the loop finishes without finding the target, return -1.
    return -1
    

my_sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_to_find = 5

result = linear_search(my_sorted_array, target_to_find)
if result == -1:
    print("Element not present")
else:
    print("element present at", result)