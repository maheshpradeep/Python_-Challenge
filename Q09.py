#simple timer

import time

user_input =int(input("Enter the seconds:"))

for x in range(user_input,0,-1):
    seconds= x % 60
    minutes = int(user_input/60) % 60
    hours = int(user_input/3600)
    
    time.sleep(1)
    
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    
print("time is up!")
    