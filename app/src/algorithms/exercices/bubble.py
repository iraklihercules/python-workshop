

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            # primary = arr[j]
            # secondary = arr[j+1]
            # if primary > secondary:
            #     arr[j] = secondary
            #     arr[j+1] = primary

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Example usage:
if __name__ == "__main__":
    # arr = [64, 34, 25, 12, 22, 11, 90]
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    bubble_sort(arr)

    print("Sorted array:", arr)  # Output: [11, 12, 22, 25, 34, 64, 90]

# <>
