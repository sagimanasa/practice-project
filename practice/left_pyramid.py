def left_pyramid(n):
    if n>0:
        print("*"*n)
        left_pyramid(n-1)
n=5
print(left_pyramid(n))

# Output:
# *****
# ****
# ***
# **
# *



