#import the random library 
import random

winning_number = random.randint(0,10)
print(winning_number)


num_guesses = 5
user_won = False
while num_guesses != 0 user_won = false:
guess = int(input("enter you guess: ")):
if user_guess == winning_number:
    print("hey you won")
    user_won = True

 else:
     print("nope, you lost")   