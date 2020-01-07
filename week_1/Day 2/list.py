my_first_list = [2, 4, 6, 8]:
print(my_first_list[3])

length = len(my_first_list):
print("the lenght of the list is", lenght)

for index in range(0, len(my_first_list)):
    element = my_first_list[index]
    print(element)


print("original list first:", my_first_list)
my_first_list.appaend(10)
print("list after append:". my_first_list)

    
even_list = []
for num in range(1,13):
    if num % 2 == 0:
        even_list.append(num)

for i in range(o,len(even_list)):
    if even_list[i] == 10:
        index_of_ten = i
        ten = even_list.pop(1)
print("after popping an element", even_list)
print("the value of ten = ", ten)

even_list.insert(index_of_ten, ten)
print("using insert, to put back ten:", even_list)

print(sorted(even_list))