def mergeSort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        middle = len(arr) // 2
        left = mergeSort(arr[:middle])
        right = mergeSort(arr[middle:])
        return merge(left, right)


def merge(arr1, arr2):
    # merge two sorted arrays into one array
    arr = []
    print(arr1, arr2)
    i1 = 0
    i2 = 0
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] < arr2[i2]:
            arr.append(arr1[i1])
            i1 += 1
        elif arr1[i1] > arr2[i2]:
            arr.append(arr2[i2])
            i2 += 1
        else:
            arr.append(arr1[i1])
            arr.append(arr2[i2])
            i1 += 1
            i2 += 1

    if i2 == len(arr2):
        arr += arr1[i1:]
    elif i1 == len(arr1):
        print(arr2[:i2])
        arr += arr2[i2:]
    return arr