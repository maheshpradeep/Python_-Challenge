#weight convertor

weight = input("select weight (kg=gram to kilogram /g=kilogram to gram):").lower()


if weight == "kg":
    
    g = float(input("enter the gram value:"))
    
    kg=g/1000;
    
    print(f"{g}g in kilogram={kg}kg")
    
    

elif weight == "g":
    
    kg = float(input("enter the kilogram value:"))
    
    g=kg*1000;
    
    print(f"{kg}kg in gram={g}g")
    
else:
    print("Please enter a valid value (kg or g)")