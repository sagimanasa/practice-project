# principle=0
# rate=0
# time=0
# while principle <=0:
#     principle=float(input("enter the principle amount:"))
#     if principle <=0:
#         print("principle can't be less than or equal or zero" )
# while rate<=0:
#     rate=float(input("enter the Interest rate:"))
#     if rate<=0:
#         print("Interest rate can't be less than or equal to zero")
# while time<=0:
#     time=int(input("enter the time in years:"))
#     if time<=0:
#         print("time can't be less than or equal to zero")
# total=principle*pow((1+rate/100),time)
# print(f"Balance after {time} years:{total:.2f}")

##another method
principle=0
rate=0
time=0
while True:
    principle=float(input("enter the principle amount:"))
    if principle <0:
        print("principle can't be less than  zero" )
    else:
        break
while True:
    rate=float(input("enter the Interest rate:"))
    if rate<0:
        print("Interest rate can't be less than  zero")
    else:
        break
while True:
    time=int(input("enter the time in years:"))
    if time<0:
        print("time can't be less than  zero")
    else:
        break
total=principle*pow((1+rate/100),time)
print(f"Balance after {time} years:{total:.2f}")
