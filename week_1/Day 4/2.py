import hashlib
import time
username = input("enter your username:")

password = "password123"
print(f"original password is: {password} ")

password=password.encode()
hashed_pw = hashlib.sha256(password).hexdigest()
print(f"hashed_pw is: {hashed_pw}")

tries = 3
waited_time = 5

successful = False

while tries >= 1 and successful == False:
    attemp = input("type in your password: ")
    attemp = attemp.encode()
    hashed_attemp = hashlib.sha256(attemp).hexdigest()
    if hashed_attemp != hashed_pw:
        #the user failed 
        tries -= 1
        print("incorrect: try again")
        print(f"you have {tries} remaining")
    else:
        print("successful logged in")
        successful = True