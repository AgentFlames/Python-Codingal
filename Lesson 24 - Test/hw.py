import random
import string

length = int(input("Enter the length of the password: "))

print("Choose character set from these: \n1.digits \n2.lowercase letters \n3.uppercase letters \n4.special characters \n5.Exit")

charlist = ""
while True: 
    option = int(input("Enter a number: "))

    if option == 1: 
        charlist += string.digits

    elif option == 2: 
        charlist += string.ascii_uppercase
        
    elif option == 3: 
        charlist += string.ascii_lowercase

    elif option == 4: 
        charlist += string.punctuation

    elif option == 5: 
        break

    else:
        print("ERROR: Invalid number")


password = []

for char in range(length): 
    randomchar = random.choice(charlist)
    password.append(randomchar)

print(f"Password : {"".join(password)}")