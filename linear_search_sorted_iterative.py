def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
    

my_sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_to_find = 5

result = linear_search(my_sorted_array, target_to_find)
if result == -1:
    print("Element not present")
else:
    print("element present at", result)