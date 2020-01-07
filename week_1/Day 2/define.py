def find_multiples(x,y,N):
    for num in range(0,N):
        if (num % x == 0) and (num % y == 0): 
            print(num)

find_multiples(3,7,100)
            



