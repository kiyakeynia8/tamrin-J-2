n = int(input())
Fibonacci = [1,1]

print(1,end=",")
print(1,end=",")

for i in range (n-2):
    a = sum(Fibonacci)
    print(a,end=",")

    del Fibonacci[0]
    Fibonacci.append(a)