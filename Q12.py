#Simple question program-02

questions=("\nQ01.What is the capital of France?",
           "\nQ02.Which is the largest planet in our solar system?",
           "\nQ03.Who wrote Romeo and Juliet?",
           "\nQ04.What is the chemical symbol for water?",
           "\nQ05.What is the square root of 16?")

q_answers=(("A. Berlin \n","B. Madrid \n","C. Paris \n","D. Rome \n"),
           ("A. Earth \n","B. Jupiter \n","C. Mars \n","D. Saturn \n"),
           ("A. Charles Dickens \n","B. William Shakespeare \n","C. Mark Twain \n","D. Jane Austen \n"),
           ("A. O2 \n","B. CO2 \n","C. H2O \n","D. N2 \n"),
           ("A. 2 \n","B. 3 \n","C. 4 \n","D. 5 \n"))

correct_answers= ("C","B","B","C","C")
given_answers = []
marks = 0
question_num = 0

print("\n---------Answer All questions---------")

for question in questions:

    print(question)
    for answers in q_answers[question_num]:
        print(answers) 
      
    answer = input("Enter the answer:").upper()
    given_answers.append(answer)
    if answer == correct_answers[question_num]:
        marks+=1
        print("Answer is correct!")
    else:
        print(f"Answer is wrong!.Correct answer is: {correct_answers[question_num]}")
    question_num +=1
    
print("--------------------------------")
   
print(f"Total marks is :{marks:02}/05")

    


