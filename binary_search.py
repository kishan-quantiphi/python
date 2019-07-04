def binarySearch(arr, l, r, x):
    if r >= l:
        mid = int(l + (r - l) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1


arr = [2, 3, 4, 10, 40]
x = int(input('enter element to search:'))
result = binarySearch(arr, 0, len(arr) - 1, x)
if result != -1:
    print(result)
else:
    raise Exception('Element not found')