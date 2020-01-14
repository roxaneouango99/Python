import random

def roll_coin():
    """
    return a coin flip: random integer between 0 and 1
    if 1 - the coin lands on head
    if 0 - the coin lands on tails
    """
    return random.randint(0,1)
def monte_carlos(n):
    """
    performs a monte carlo stimulation of a coin flip
    [PARAM]\t n (int) - number of samples
    [Return]\t - none prints out the results of the stimulation
    """
head_count = 0
tail_count = 0
exp_count = 0
while exp_count < n:
    result = flip_coin()
    if result == 1:
        head_count += 1
    else:
        tail_count += 1
    exp_count += 1

   

msg = f"there were{(head_count)/n) * 100} % heads"
print(msg)
msg = f"there were {(tail_count)/n) * 100} %tails"
print(msg)

monte_carlos(1000)
help(monte_carlos)