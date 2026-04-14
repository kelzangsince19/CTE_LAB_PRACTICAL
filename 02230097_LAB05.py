def sequential_search(arr, target):
    comparisons = 0
    
    for index in range(len(arr)):
        comparisons += 1
        if arr[index] == target:
            return index, comparisons
    
    return -1, comparisons


# Example usage
arr = [23, 45, 12, 67, 89, 34, 56]
target = 67

index, comparisons = sequential_search(arr, target)

print("List:", arr)
print("Searching for", target, "using Sequential Search")

if index != -1:
    print("Found at index", index)
else:
    print("Not found")

print("Number of comparisons:", comparisons)

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    comparisons = 0
    
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons


