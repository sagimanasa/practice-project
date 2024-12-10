#shopping cart program

foods=[]
prices=[]
total=0
while True:
    food=input("enter the food you want:")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"enter the price of {food}:$"))
        foods.append(food)
        prices.append(price)
print("------your cart-------")
for food in foods:
    print(food,end=" ")
for price in prices:
    total+=price
print()
print(f"the total price is :${total}")


