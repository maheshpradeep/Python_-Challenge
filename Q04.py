#simple calculator

user_option = input("enter the operator(+ , - ,/ , * ) :  ")

num1 = float(input("enter the number 01:"))
num2 = float(input("enter the number 02:"))



if user_option == "+" :
    
    result = num1+num2
    print(f"{num1} + {num2}= {round(result,3)}")
    
elif user_option == "-" :
    
    result = num1-num2
    print(f"{num1} - {num2}= {round(result,3)}")
    
elif user_option == "/" :
    
    if num2==0:
        
        print(" can't divide by 0")
        
    else:
    
        result = num1/num2
        print(f"{num1} / {num2}= {round(result,3)}")
        
elif user_option == "*" :
    
    result = num1*num2
    print(f"{num1} * {num2}= {round(result,3)}")      

else:
    print("enter correct operator")
