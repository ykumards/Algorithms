"""
Multiply two number recursively, without using *.
Runtime is O(k) where k is the minimum of the two operands
"""

def _naive_recMult(addr, multer):
    if multer == 0:
        return 0
    addr += _naive_recMult(addr, multer-1)
    return addr

def recMult(a, b):
    small = min(a,b)
    big = max(a,b)
    return _recMult(big, small)

# While naive method was O(k), we can reduce this to O(log k)
# 20 * 4 = 20 * 2 + 20 * 2 = 20 * 1 + 20 * 1 + 20 * 1 + 20 * 1
# This is basically the same as last method, but we double each 
# result instead of adding subsequent values.
# This gets us the O(log k) runtime. But we still have to handle 
# the case when k is odd. For this, simply use:
# 20 * 5 = 20 * 2 + 20 * 2 + 20
def _recMult(big, small):
    if small == 0:
        return 0
    if small == 1: # for 1 * big
        return big
    half = small >> 1 # Binary shifting basically does integer division by 2
    half_prod = _recMult(half, big)
    if small % 2 == 0:
        return half_prod << 1
    else:
        return (half_prod << 1) + big

if __name__ == "__main__":
    print "10 x 2:", recMult(10,2)
    print "3 x 1000:", recMult(3,1000)
    print "1212 x 9891:", recMult(1212, 9891)
