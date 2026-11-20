import random
letter = "abcdefghijklmnopqrstuvwxyz"
number = "1234567890"
symbols = "!@#$%^&*()_-+={}[]|:;<>,.?/"
password_length = int(input("How many letters would you like in your password?"))
password_number = int(input("How many numbers would you like in your password?"))
password_symbols = int(input("How many symbols would you like in your password?"))
password_list = []
for i in range(password_length):
    password_list.append(random.choice(letter))
for i in range(password_number):
    password_list.append(random.choice(number))
for i in range(password_symbols):
    password_list.append(random.choice(symbols))
print(password_list) 
random.shuffle(password_list)
print(password_list)
password = ""
for i in password_list:
    password += i
print(f"Your password is: {password}")