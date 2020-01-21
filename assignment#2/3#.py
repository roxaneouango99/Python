def numberfromstring(my_string):

    n=list(my_string)
    for i in n:
        if i.isdigit():
            num =int(i)
            print(num)

my_string = "bob has 1 donut and 16 coffees"
print(numberfromstring(my_string))                                                                                                                                         
