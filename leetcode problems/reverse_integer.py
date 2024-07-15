def is_reverse(x):
    is_negative = x < 0
    x = abs(x)
    reversed_num = 0
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    if is_negative:
        reversed_num = -reversed_num
    return reversed_num
x = -123
print(is_reverse(x))
# print(f"The reverse of {x} is {is_reverse(x)}")
#input:123 output:321
#input:-123 output:-321
