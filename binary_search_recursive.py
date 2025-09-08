def binary_search(arr, target, low, high):
    
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    
    elif target < arr[mid]:
        return binary_search(arr, target, low , mid - 1)
    
    else:
        return binary_search(arr, target, mid + 1, high)
    


# my_sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# target_to_find = 23
# result = binary_search(my_sorted_list, target_to_find, low = 0, high = len(my_sorted_list) - 1)
    
# if result != -1:
#     print(f"Iterative Binary Search: Target {target_to_find} was found at index: {result} if counting starts from 0")
# else:
#     print(f"Iterative Binary Search: Target {target_to_find} was not found.")

def binary_search_wrapper(arr, target):
    """A user-friendly wrapper to start the recursive binary search."""
    return binary_search(arr, target, 0, len(arr) - 1)

# --- Example Usage ---
if __name__ == "__main__":
    my_sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

    # --- Search for an item that exists ---
    target_to_find = 38
    result = binary_search_wrapper(my_sorted_list, target_to_find)
    
    if result != -1:
        print(f"Recursive Binary Search: Target {target_to_find} was found at index: {result}")
    else:
        print(f"Recursive Binary Search: Target {target_to_find} was not found.")