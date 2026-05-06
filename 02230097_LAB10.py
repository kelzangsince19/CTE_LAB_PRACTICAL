#part1
def counting_sort(arr):
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1

    # Step 1: Count occurrences of each value
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1

    # Step 2: Reconstruct the sorted array
    sorted_arr = []
    for i, freq in enumerate(count):
        sorted_arr.extend([i + min_val] * freq)

    return sorted_arr


# Example usage
arr = [2, 5, 3, 0, 3, 0, 3]
print(counting_sort(arr))   # [1, 2, 2, 3, 3, 4, 8]

#part 2
def counting_sort(arr, exp):
    n = len(arr)

    # Output array
    output = [0] * n

    # Count array (for digits 0–9)
    count = [0] * 10

    # Count occurrences of digits
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Convert count to cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array (stable sort)
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy back to original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # Find maximum number to know number of digits
    max_num = max(arr)

    exp = 1  # 1, 10, 100, ...

    # Apply counting sort for each digit
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr

arr = [53, 89, 150, 36,633, 233]
print(radix_sort(arr))
