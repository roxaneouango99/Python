def roll_dice():
def monte_carlos_with_list(N, dice_max=6):
    result = []

   
    for exp in range (0, N):
        result.append(roll_dice(dice_max))
    print(f"{N} experiments were performed")   
    for outcome in range(1,dice_max + 1):
        count = result.count(outcome)
    

        msg = f"the probanility of {outcome} = {(count/N * 100)} %"
        print(msg)

dice_max = 10
print(f"the probability should converge to {(1/dice_max  * 100)} %")
monte_carlos_with_list(10000, dice_max)