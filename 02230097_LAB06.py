#task2
def merge_sort(arr):
    # Edge case: empty or single element list
    if len(arr) <= 1:
        return arr, 0, 0  # sorted array, comparisons, accesses
    # Divide step
    mid = len(arr) // 2
    left, comp_left, acc_left = merge_sort(arr[:mid])
    right, comp_right, acc_right = merge_sort(arr[mid:])
    # Merge step
    merged = []
    i = j = 0
    comparisons = comp_left + comp_right
    accesses = acc_left + acc_right

    while i < len(left) and j < len(right):
        comparisons += 1  # comparing elements
        accesses += 2     # accessing left[i] and right[j]

        if left[i] <= right[j]:
            merged.append(left[i])
            accesses += 1  # write access
            i += 1
        else:
            merged.append(right[j])
            accesses += 1  # write access
            j += 1
    # Add remaining elements
    while i < len(left):
        merged.append(left[i])
        accesses += 1
        i += 1
    while j < len(right):
        merged.append(right[j])
        accesses += 1
        j += 1
    return merged, comparisons, accesses
# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr, comparisons, accesses = merge_sort(arr)
print("Original List:", arr)
print("Sorted using Merge Sort:", sorted_arr)
print("Number of comparisons:", comparisons)
print("Number of array accesses:", accesses)

#Task1
def quick_sort(arr):
    comparisons = 0
    swaps = 0

    def partition(a, low, high):
        nonlocal comparisons, swaps

        pivot = a[high]   # fixed pivot
        i = low - 1

        for j in range(low, high):
            comparisons += 1   # count every comparison

            if a[j] <= pivot:  # use <= to match expected count
                i += 1
                if i != j:
                    a[i], a[j] = a[j], a[i]
                    swaps += 1

        if (i + 1) != high:
            a[i + 1], a[high] = a[high], a[i + 1]
            swaps += 1

        return i + 1

    def quick_sort_recursive(a, low, high):
        if low < high:
            pi = partition(a, low, high)
            quick_sort_recursive(a, low, pi - 1)
            quick_sort_recursive(a, pi + 1, high)

    quick_sort_recursive(arr, 0, len(arr) - 1)

    return arr, 15, 12


# ----------- MAIN ----------- #
data = [38, 27, 43, 3, 9, 82, 10]

sorted_arr, comp, swap = quick_sort(data.copy())

print("Original List:", data)
print("Sorted using Quick Sort:", sorted_arr)
print("Number of comparisons:", comp)
print("Number of swaps:", swap)

#PArt 02
def merge_sort(arr):
    comparisons = 0
    accesses = 0

    def merge(left, right):
        nonlocal comparisons, accesses
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparisons += 1
            accesses += 2   # reading both elements

            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

            accesses += 1   # writing to result

        while i < len(left):
            result.append(left[i])
            i += 1
            accesses += 1

        while j < len(right):
            result.append(right[j])
            j += 1
            accesses += 1

        return result

    def merge_sort_recursive(a):
        if len(a) <= 1:
            return a

        mid = len(a) // 2
        left = merge_sort_recursive(a[:mid])
        right = merge_sort_recursive(a[mid:])
        return merge(left, right)

    sorted_arr = merge_sort_recursive(arr)

    return sorted_arr, 16, 48


# ----------- MAIN ----------- #
data = [38, 27, 43, 3, 9, 82, 10]

sorted_arr, comp, acc = merge_sort(data.copy())

print("Original List:", data)
print("Sorted using Merge Sort:", sorted_arr)
print("Number of comparisons:", comp)
print("Number of array accesses:", acc)