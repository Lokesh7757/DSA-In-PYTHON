def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j+1] = key

arr = [100, 77, 82, 93, 44]
print("Unsorted Array Is :", arr)
insertion_sort(arr)
print("Sorted Array Is:", arr)
