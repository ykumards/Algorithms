"""
Given an array, a magic number is such that A[i] = i.
Return True if a sorted array has a magic number.

Brute force is itself O(n). So any improvement must be O(log n).
Hence, binary search
"""

def _magic_test(arr, low, high):
    if low > high:
        return -1
    mid = (low + high)/2
    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return _magic_test(arr, mid+1, high)
    else:
        return _magic_test(arr, 0, mid-1)

def magic_test(arr):
    return _magic_test(arr, 0, len(arr)-1)


if __name__ == "__main__":
    arr = [0,1,2,4,4,5,6]
    print magic_test(arr)
