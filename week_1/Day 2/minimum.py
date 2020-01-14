def find_min(list):
    min = list[0]
    for i in range(0,len(list)):
        if list[i] < min:
            min = list[i]

    return min

my_list =[1, 2, 3] 
print(find_min(my_list))       
        

