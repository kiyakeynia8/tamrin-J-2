import random

computer_score = 0
user_score = 0

while computer_score < 5 and user_score < 5:
    
    x = random.randint(1, 3)
    if x == 1:
        computer =  "rock"

    if x == 2:
        computer = "paper"

    if x == 3:
        computer = "scissors"

    print("---------------")
    print("rock")
    print("paper")
    print("scissors")
    print("---------------")

    user = input()


    if computer == "rock" and user == "paper":
        print("user win")
        user_score = user_score + 1

    elif computer == "rock" and user == "scissors":
        print("computer win")
        computer_score = computer_score + 1
        
    elif computer == "rock" and user == "rock":
        print("try again")
        
    elif computer == "paper" and user == "paper":
        print("try again")
        
    elif computer == "paper" and user == "scissors":
        print("user win")
        user_score = user_score + 1
        
    elif computer == "paper" and user == "rock":
        print("computer win")
        computer_score = computer_score + 1
        
    elif computer == "scissros" and user == "paper":
        print("computer win")
        computer_score = computer_score + 1
        
    elif computer == "scissors" and user == "scissors":
        print("try again")
        
    elif computer == "scissors" and user == "rock":
        print("user win")
        user_score = user_score + 1

    print("computer =", computer)
    print("---------------")
    print("computer score =",computer_score)
    print("user score =",user_score)        
