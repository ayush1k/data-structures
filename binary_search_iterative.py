def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
            
    return -1

my_sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_to_find = 23
result = binary_search(my_sorted_list, target_to_find)
    
if result != -1:
    print(f"Iterative Binary Search: Target {target_to_find} was found at index: {result} if counting starts from 0")
else:
    print(f"Iterative Binary Search: Target {target_to_find} was not found.")