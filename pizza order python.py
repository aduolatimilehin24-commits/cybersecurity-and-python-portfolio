print("WELCOME TO TIMI's PIZZA DELIVERIES")
bill = 0
size = input("what is the size? S,M or L")
if size ==  "S":
      bill += 12
elif size == "M":
      bill += 15
elif size == "L":
      bill += 16
peperoni = input("do you want peperoni on ur pizza? Y or N")
if peperoni == "Y":
      bill +=2
elif peperoni == "N":
    bill += 0
extracheese = input("do you wan cheese? Y or N")
if extracheese == "Y":
      bill += 1
elif extracheese == "N":
      bill += 0
print(f"your bill is ${bill}")