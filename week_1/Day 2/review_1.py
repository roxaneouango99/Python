# to do a script that print out the multiple of 3 
#between 0 and N where N is a user input 

N = int(input("enter the upper limit."))

for num in range(0,N+1):
   if num %3 == 0:
        print(num)