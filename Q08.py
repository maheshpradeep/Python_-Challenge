#interest calculator 

principle = 0
rate=0
time=0


while True :
    principle=float(input("enter the principle value:"))
    
    if principle < 0:
        print("you are not enter the correct value!")
        
    else:
        break
    
while True:
    rate=float(input("enter the rate value:"))
    
    if rate < 0:
        print("you are not enter the correct value!")
        
    else:
        break
        
while True:
    time=float(input("enter the time:"))
    
    if time < 0:
        print("you are not enter the correct value!")    
        
    else:
        break   
        
        
total = principle * pow((1+rate/100),time)

print(f"Total interest for {time} years:${total:.2f}")