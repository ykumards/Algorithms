import random
import timeit

def qsort(arr):
    if len(arr) < 2:
        return arr

    less = []
    more = []
    equal = []
    p = arr[0]
    for x in arr:
        if x < p:
            less.append(x)
        elif x > p:
            more.append(x)
        else:
            equal.append(x)

    return qsort(less) + equal + qsort(more)

if __name__ == "__main__":
    start = timeit.default_timer()
    arr = [random.randint(0, 1000) for _ in xrange(10000)]
    result = qsort(arr)
    #print result
    print "Runtime:", (timeit.default_timer() - start)
