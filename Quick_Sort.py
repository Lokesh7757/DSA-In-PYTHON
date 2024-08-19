def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


arr = [3, 6, 8, 10, 1, 2]
print("Unsorrted array is:", arr)
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
