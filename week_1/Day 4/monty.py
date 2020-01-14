import random

def organize_game():
    door_contents = [1, 0, 0]
    random.shuffle(door_contents)

    for i in range(0, len(door_contents)):
        if door_contents[i] == 1:
            winning_door = i

    return door_contents, winning_door

def game_time():
    doors_num = [0, 1, 2] 

    door_contents, winning_door = organize_game() 

    # we need the contestant to make a choice

    door_chosen = random.choice(doors_num)  
    # we need the game show host to open another door
    #the game show host must open a door that does not have the winning door
# make a liost of unavailable door to open
    unavailable_door = [door_chosen, winning_door]
    # using set 
    door_to_open = set(doors_num).difference(unavailable_door)
    # pop to return this door_open as a set
    door_to_open  = door_to_open.pop()

    opened_door = doors_num[door_to_open]
    #see if the cont won or lost

    switched_win = False
    stayed_win = False  
    unavailable_door = [door_chosen, door_to_open]
    switched_choice = set(doors_num).difference(unavailable_door)
    switched_choice = switched_choice.pop()


    #use the index value etablished to find the content of the door behind
    if door_contents[switched_choice] == 1:
        switched_win = True
    if door_contents[door_chosen] == 1:
        stayed_win = True 
    return int(switched_win), int(stayed_win)

def monte_carlo(N):
#   # keep track of number
    total_switched_win = 0
    total_stayed_win = 0

    switched_win = 0
    stayed_win = 0
    for game_num in range(0,N):

        switched_win, stayed_win = game_time()
        if switched_win == 1:
            total_switched_win += 1

        if stayed_win == 1:
            total_stayed_win += 1

    print(f"out of {N} plays")
    print(f"switched win percentage = {(total_switched_win/N *100)} %")
    print(f"stayed win percentage = { total_stayed_win/N *100} %")

monte_carlo(100000)







