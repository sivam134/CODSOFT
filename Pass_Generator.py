import random
char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_?:<>"
while(1):
    pass_length=int(input("Enter the length of the password: "))
    password=""
    for i in range(pass_length):
        password_char=random.choice(char)
        password=password+password_char
    print(f"This is your password: {password}")
    repeat=input("Do you want to generate another password?\n(Yes/No)")
    if repeat.lower() == "no":
        break