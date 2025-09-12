# a+b = 1000

def two_sum(arr, target=1000):
    n = len(arr)
        
    for i in range(n):
        low = i+1
        high = n - 1
        complement = target - arr[i]
        while low <= high:   
            mid = (low+high)//2         
            if arr[mid] == complement:
                return arr[i], complement
            elif arr[mid] > complement:
                high = mid - 1
            else:
                low = mid + 1
    return -1


# --- Example Usage ---
if __name__ == "__main__":
    my_array = [20, 70, 90, 150, 400, 600, 850, 910]
    result = two_sum(my_array)
    
    if result:
        print(f"Binary Search: Found pair {result} that sums to 1000.")
    else:
        print("Binary Search: No pair found.")