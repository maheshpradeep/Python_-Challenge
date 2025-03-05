#Hotel menu ,Order with bill program

menu = {"Chips":300.00,
        "Coffee":60.00,
        "Tea":70.00,
        "Burger":150.00,
        "HotDog":200.00,
        "Egg roll":100.00,
        }

buy_items=[]

value=[]

Quantity=[]


print("-------Price List---------")

for item,price in menu.items():
    print(f"{item:10} : {price:.2f}")
    
print()
    
    
while True:
    buy = input("Enter the item:")


    if buy == "q":
        break
    
    elif buy in menu:
        
        qty = (int(input("Quantity :")))
        buy_items.append(buy)
        Quantity.append(qty)
        value.append(menu[buy]*qty)
    
    else:
        print("Item not in the menu!")   
        
total=sum(value) 
      
print("-------Total Bill---------")
print(f"Items \t Quantity     value" )
        
for i in range (len(buy_items)):
    

    print(f"{buy_items[i]} \t {Quantity[i]} \t - {value[i]:.2f}" )

print()

print(f"Total value\t :{total:.2f}")



    


