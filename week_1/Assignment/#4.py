# programming challenge 4:
#  find the difference between two list

def find_diff(a,b):
    differences = []
    for element in a:
        if element not in b:
            differences.append(element)
        return differences

test1 = [1, 2, 3] 
test2 = [4, 5, 6]       
print(find_diff(test1,test2))