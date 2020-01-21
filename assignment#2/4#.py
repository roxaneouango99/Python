list = []
num = int(input('How many numbers: '))

for n in range(num):
    numbers = int(input('Enter number '))
    if numbers%2==1:
        list.append(numbers)

print("Max odd num in the list is :", max(list), "\nMin odd num in the list is :", min(list))
print("the sum of odd num in the list and min num in the list is:", sum(list))
