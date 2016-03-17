import math

def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)

# for num in range(3, 10):
#     print num, nCr(num, 3) * 2


# 3 2
# 4 8
# 5 20
# 6 40
# 7 70
# 8 112
# 9 168