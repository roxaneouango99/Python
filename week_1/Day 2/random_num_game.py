#import the random library 
import random

winning_number = random.randint(0,10)
print(winning_number)


num_guesses = 5
user_won = False
while num_guesses != 0 and user_won == False:
    guess = int(input("enter you guess: "))
    if guess == winning_number:
        print("hey you won")
        user_won = True
    else:
        num_guesses -= 1
        if (num_guesses != 0):
            print("try again")
        else:
            print("nope, you lost!")   