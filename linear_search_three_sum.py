# a+b+c = 1000
# using the brute force approach / linear search
def three_sum(arr, target = 1000):
    n = len(arr)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == 1000:
                    return arr[i], arr[j], arr[k]
                
    return -1

if __name__ == "__main__":
    my_array = [20, 70, 90, 150, 400, 600, 850, 910] # 90 + 150 + 850 = 1090
    my_array_2 = [10, 20, 370, 500, 610, 900] # 10 + 370 + 610 = 990
    my_array_3 = [50, 100, 250, 650, 800] # 100 + 250 + 650 = 1000
    
    result = three_sum(my_array_2)
    
    if result:
        print(f"Brute-Force: Found triplet {result} that sums to 1000.")
    else:
        print("Brute-Force: No triplet found.")
