# n=15
# if n>0:
#     print("positive")
# elif n<0:
#     print("negative")
# else:
#     print("zero")
#
# # output:positive

def check_number(n):
    if n>0:
        return "positive"
    elif n<0:
        return "negative"
    else:
        return "zero"
n=-2
print(check_number(n))
#output:negative