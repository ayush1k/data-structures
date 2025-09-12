# a+b=1000
def linear_search_two_sum(arr,target=1000):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == target:
                return arr[i], arr[j]
    
    return -1

if __name__ == "__main__":
    my_array = [20, 70, 90, 150, 400, 600, 850, 910]
    result = linear_search_two_sum(my_array)
    
    if result:
        print(f"Brute-Force: Found pair {result} that sums to 1000.")
    else:
        print("Brute-Force: No pair found.")