# a+b+c = 1000
# using the binary search approach

def three_sum(arr, target = 1000):
    n = len(arr)
    
    for i in range(n-2):
        for j in range(i+1, n-1):
            
            complement = target - arr[i] - arr[j]
            
            low = j+1
            high = n - 1
            
            while low <= high:
                mid = (low+high)//2
                
                if arr[mid] == complement:
                    return arr[i], arr[j], arr[mid]
                elif arr[mid] < complement:
                    low = mid + 1
                else:
                    high = mid - 1
    
    return -1


if __name__ == "__main__":
    my_array = [50, 100, 250, 650, 800] # 100 + 250 + 650 = 1000
    result = three_sum(my_array)
    
    if result:
        print(f"Binary Search: Found triplet {result} that sums to 1000.")
    else:
        print("Binary Search: No triplet found.")