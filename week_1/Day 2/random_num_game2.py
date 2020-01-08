#import the random library
import random

winning_number = random.randint(0, 100)
print("the winning number is", winning_number)
total_guess = 10
guesses =[]
user_won = False
number_guess = 0


while number_guess < total_guess and user_won == False:
    user_guess = int(input("enter your guess: "))
    guesses.append(number_guess)
    number_guess  += 1
    if number_guess == winning_number:
        user_won = True
        print("congrat you won!")
    elif user_guess >= winning_number -5 and user_guess <= winning_number +5:
        print("hot")
    elif user_guess >= winning_number -10 and user_guess <= winning_number +10:
        print("warm")
    else:
        print("cold.")


print("you took", total_guess)

    
