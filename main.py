import random
char = "qwertyuiopasdfghjklzxcvbnm!@#$%^&*(){}[]"
long = input("Total number of passowrds? : ")
long = int(long)
for p in range(long):
    length = int(input("Password length: " ))

    password = ''
    for c in range(length):
        password += random.choice(char)
    print(password)

