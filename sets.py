my_set1 = {1, 2, 3, 4}
my_set2 = {4, 5, 6, 7}
my_set3 = {8, 9, 12, 45, 1, 6}

#  Union
my_set4 = my_set1.union(my_set2)
# my_set4 = my_set1 | my_set2
print(my_set4)


# Intersection
my_set5 = my_set3 & my_set2
# my_set5  = my_set3.intersection(my_set2)
print(my_set5)


# Diferencia
my_set6 = my_set4 - my_set2
# my_set6 = my_set4.difference(my_set2)
print(my_set6)

# diferencia simetrica
# es lo contrario de la interseccion 
my_set7 = my_set4 ^ my_set5 ^ my_set6
# my_set7 = my_set4.symmetric_difference(my_set5)  Only 2 sets
print(my_set7)