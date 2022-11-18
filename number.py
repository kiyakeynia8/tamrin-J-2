import random

computer = random.randint(1, 50)

for i in range(1, 11):

    user = int(input("guess a number: "))

    if computer == user:
        print("you win")
        print(i)
        break
        

    elif computer > user:
        print("Go up")

    elif computer < user:
        print("Come down")

if i == 10:    
    print("Game over")