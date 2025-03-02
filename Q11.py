#Simple question program

questions=["\nQ01.What is the capital of France?",
           "\nQ02.Which is the largest planet in our solar system?",
           "\nQ03.Who wrote Romeo and Juliet?",
           "\nQ04.What is the chemical symbol for water?",
           "\nQ05.What is the square root of 16?"]

q_answers=["A. Berlin \nB. Madrid \nC. Paris \nD. Rome \n",
           "A. Earth \nB. Jupiter \nC. Mars \nD. Saturn \n",
           "A. Charles Dickens \nB. William Shakespeare \nC. Mark Twain \nD. Jane Austen \n",
           "A. O2 \nB. CO2 \nC. H2O \nD. N2 \n",
           "A. 2 \nB. 3 \nC. 4 \nD. 5 \n"]

correct_answers= ["C","B","B","C","C"]

i=0

marks = 0

print("\n---------Answer All questions---------")

for i in range(len(questions)):
    print(questions[i])
    print(q_answers[i])
    
    ans=input("enter the answer:").upper()
        
    if ans == correct_answers[i]:
            
            marks=marks+1
            print("Answer is correct!")
    else:
        print(f"Answer is wrong!.Correct answer is:{correct_answers[i]}")
print()

print("--------------------------------")
   
print(f"Total marks is :{marks:02}")

