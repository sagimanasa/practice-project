def right_pyramid(n):
    for i in range(0, n):
        for j in range(0, n - i - 1):
            print(" ", end="")
        for k in range(0, i + 1):
            print("*", end="")
        print()
n = 5
print(right_pyramid(n))

# Output:
#     *
#    **
#   ***
#  ****
# *****