import random

simbols = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
lenght = int(input("какой длины вам нужен пароль"))
pasword = ""
for i in range(lenght):
    pasword += random.choice(simbols)
print(pasword)
