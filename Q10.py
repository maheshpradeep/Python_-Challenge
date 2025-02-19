#simple shopping cart program

foods=[]
prices=[]
qtys=[]
total=0

while True:
    food=(input("Enter the food(if want quit press q):"))
    
    if food.lower() == "q":
        break
    else:
        qty = (float(input(f"Enter the {food} qty:")))
        price = (float(input(f"Enter the {food} price:")))
        
        
        foods.append(food)
        qtys.append(qty)
        prices.append(price)
        

print("-----------food cart-----------\n")

for f in range(len(foods)):
    
    item_price = qtys[f] * prices[f]
    total=total+item_price
        
    print(f"item\tqty\tprice\ttotal item price\n {foods[f]}\t{qtys[f]:.2f}\t{prices[f]:.2f}\t{item_price:.2f}")
    
    print()
    
print(f"Total bill value is:{total:.2f}")