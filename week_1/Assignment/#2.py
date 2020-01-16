def odds(N):
    odds: []

    for number in range(0,N+1):
        if (number % 2 == 1):
            odds.append(number)

    return odds
n = 5
print(odds(5))
