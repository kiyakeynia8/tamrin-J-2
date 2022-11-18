Scores = []

while True:
    a = input("baray khrej shodan tayp kon ""exit"".....baray mondan type kon ""Stay"": ")
    if a == "exit":
        b = sum(Scores)
        c = len(Scores)
        d = b / c
        print("your average = ",d)
        break

    else:    
        g = float(input("enter your Score: "))
        Scores.append(g)