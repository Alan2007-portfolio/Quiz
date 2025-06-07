import random
print("This is a 5Q quiz ")
print("You will be answering 5 question worth 2 mark each")
print("you will also be having a bonus question which is worth 5 marks  as a game changer which will be optional")
print("The total marks for this quiz is 10") #10 marks from the 5 questions and 5 marks from the bonus questions(if your points are less than 5)
print("Best of luck")
points=0
def bonus():
    global points #so tha we can use the variable "points" which was defined outside def
    bonus_Q=[("what is the last letter of the alphabet ? ","z"),
             ("what number comes after 16? ",17),
             ("where is the Eiffel Tower located? ","Paris")]
    question,answer=random.choice(bonus_Q)
    your_answer=input(f'{question}').strip().lower()
    if isinstance(answer,int): #This for answers which are int 
        try:
            if int(your_answer)==answer:
                print("you are right")
                points+=5
            else:
                print('sorry,wrong answer')
        except ValueError: #if the answer is not converted to int 
            print('invalid input')
    else: #For answers that are string
        if your_answer==answer:
            print("you are right")
            points+=5
        else:
            print('sorry,wrong answer')
def questions():
    global points 
    a=int(input("What is the number after 1?"))
    if a==2:
        print("The answer is correct ")
        print("You have scored 2 points")
        points+=2
    else:
        print("Incorrect answer")
    b=input("What is the alphabet after c?").lower() #.lower() makes sure that we can use both small and capital letters
    if b=='d':
        print("The answer is correct ")
        print("You have scored 2 points")
        points+=2
    else:
        print("Incorrect answer")
    c=int(input("What is the number after 5?"))
    if c==6:
        print("The answer is correct ")
        print("You have scored 2 points")
        points+=2
    else:
        print("Incorrect answer")
    d=int(input("What is the number after 7?"))
    if d==8:
        print("The answer is correct ")
        print("You have scored 2 points")
        points+=2
    else:
        print("Incorrect answer")
    e=int(input("What is the number after 10?"))
    if e==11:
        print("The answer is correct ")
        print("You have scored 2 points")
        points+=2
    else:
        print("Incorrect answer")
    
    print("")
    if points<=5:#the bonus question will only be asked if the user's point is less than or equal to 5, so that even with bonus mark it will total up to 10 as mentioned before
        v=input("Do you want to answer the bonus question, type yes or no :  ").strip().lower()
        if v=='yes':
            print('here is your bonus question')
            bonus() #If the condition is met the Bonus Function defined above will be called
        else:
            print("your quiz is over.")

        print('Thankyou for participating')
    else:
        print('Your quiz is over')
   
questions()


print('Congrats')
print('your total points:',points)
if points>=10:
    print('Congrats u have passed the quiz with flying colors')
elif 5 <= points < 10:
    print('Good work')
else:
    print('betterluck next time , keep up the good work')