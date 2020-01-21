def find_min(list):
    min = list[0]
    for i in range(0,len(list)):
        if list[i] <= min:
            min = list[i]

    return min

my_list =[2.5, 6.2, 3.14] 
print(find_min(my_list))       
        