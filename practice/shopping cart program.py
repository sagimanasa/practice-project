item=input("what item would you like to buy?:")
price=float(input("what is the price?:"))
quantity=int(input("how many would you like?:"))
total=price*quantity
print(f"you have bought {quantity}*{item}/s")
print(f"your total is {total}")

# ouput:
# what item would you like to buy?:pizza
# what is the price?:11.98
# how many would you like?:6
# you have bought 6*pizza/s
# your total is 71.88