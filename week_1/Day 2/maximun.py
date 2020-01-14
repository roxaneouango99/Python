def find_max(list):

    """
    this function returns he maximun element in the list

    \tparam : list - a list of numerical elements
    \treturn : the maximum value in the list
    
    """
    max = list[0]
    for i in range(0,len(list)):
        if list[i] >= max:
            max = list[i]

    return max

my_list =[1, 2, 3] 
print(find_max(my_list))       
        


