"""
Given the total number of steps, find the number of possible
ways to reach the nth step if we're only allowed to take
1,2 or 3 steps at a time.
Notes:
Helps to think of this problem top-down. Starting from the last step, the number of ways
to reach there is the sum of the number of ways to reach (n-1), (n-2) and (n-3)
"""
def counting_steps(n, arr):
    if n < 0:
        return 0
    if n == 1:
        return 1
    if arr[n] > -1:
        return arr[n]
    else:
        arr[n] = counting_steps(n-1, arr) + counting_steps(n-2, arr) + counting_steps(n-3, arr)
        return arr[n]


if __name__ == "__main__":
    n = 20
    arr = [-1 for _ in range(20)]
    print "Number of ways: ", counting_steps(n-1, arr)
        
