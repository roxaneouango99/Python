def find_evens(a,b):
    evens = []
    for num in range(a,b+1):
        if num % 2 == 0:
            evens.append(num)
            return(num)
print(find_evens(2,100))
            
