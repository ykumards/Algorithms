def mergeSort(arr):
    if len(arr) < 2:
        return arr

    mid = int(len(arr) / 2)
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)
     

def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


if __name__ == "__main__":
    arr = [3,2,23,1,34,15,9,12]
    print mergeSort(arr)

