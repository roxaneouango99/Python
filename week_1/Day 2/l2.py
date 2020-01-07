def find_even(a,b):
    even = []
    for num in range(a,b+1):
        if (num % 3 == 0) and (num % 2 == 0):
            even.append(num)
            return(num)

print(find_even(0,100))
