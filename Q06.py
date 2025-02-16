#temperature convertor 

selection= input("Select fahrenheit  or celsius (F/C)").upper()

if selection in ["F","C"]:

    temperature = float(input("Enter temperature value:"))

if selection == "F":
    
    C=(temperature-32)/(9/5)
    
    print(f"Celsius value is = {C}C°")
    
    
elif selection == "C":
    
    F=temperature*(9/5)+32
    
    print(f"Fahrenheit value is = {F}F°")
    
else:
    
    print("Enter correct selection")
