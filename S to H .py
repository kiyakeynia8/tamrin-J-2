s = int(input("enter S : "))

h = s // 3600
print("H = ",h)
f = s % 3600
m = f // 60
print("M = ",m)
s = f % 60
print("S = ",s)