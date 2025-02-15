#calculate circumference and area 

import math

r=float(input("give the radius value:"))

cir=2*math.pi*r
area=math.pi*pow(r,2)

print(f"circumference value is:{round(cir,2)}")
print(f"area is :{round(area,2)}" )
