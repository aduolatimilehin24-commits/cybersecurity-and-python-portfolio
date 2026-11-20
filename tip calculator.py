print("WELCOME TO THE TIP CALCULATOR")
A = int(input("what is the total value? "))
B = int(input(" what amount do you want to tip: 10, 12, 15? "))
C = B/100*A
F = C+A
D = int(input("enter the amount of people that sharing the bill? "))
E = F/D
print(E)