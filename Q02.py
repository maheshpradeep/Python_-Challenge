#Shopping cart item programme
#item,price,qty

item=input("please enter the item:")
price=float(input("please enter the price:"))
qty=int(input("please enter the qty:"))

total_price=price*qty

print(f"item {item} total price is rs.{total_price}")