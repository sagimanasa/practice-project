def recursion(n):
    if n==0:
        return n
    return n+recursion(n-1)
n=6
print(recursion(n))
# output=21
# recursion(6) returns 6 + recursion(5)
# recursion(5) returns 5 + recursion(4)
# recursion(4) returns 4 + recursion(3)
# recursion(3) returns 3 + recursion(2)
# recursion(2) returns 2 + recursion(1)
# recursion(1) returns 1 + recursion(0)
# recursion(0) returns 0 (base case)
# recursion(0) = 0
# recursion(1) = 1 + 0 = 1
# recursion(2) = 2 + 1 = 3
# recursion(3) = 3 + 3 = 6
# recursion(4) = 4 + 6 = 10
# recursion(5) = 5 + 10 = 15
# recursion(6) = 6 + 15 = 21