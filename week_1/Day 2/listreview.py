def search(x, list):
    """ 
    this function return the index of where the element x was found on the list
    """
for index in range(0,len(list)):
    if my_list [index] == x:
         return index

my_list = [1, 2, 3, 4, 5]
ans = search(1, my_list)
print(ans)