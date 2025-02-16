#valid user input
#input must 12 characters,no space,no digits

username=input("Enter the username:")

length=len(username)
space=username.find(" ")
digits=username.isalpha()


if length>12:
    print("your user name only contain 12 characters") 

elif space > -1:
    print("you can't contain space ")    
    
elif digits == 0 :
     print("you can't contain digits ") 
     
else:
    print(f"welcome to the world {username}!")

