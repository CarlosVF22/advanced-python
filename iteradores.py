my_list = [1,2,3,4,5]
my_iter = iter(my_list)


#  ciclo for es sugar sintax del siguiente ciclo while
for element in my_list:
    pass

#  ---------------------
while True:
    try:
        element = next(my_iter)
        print(element)
    
    except StopIteration:
        break
# -------------------------