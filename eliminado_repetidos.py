def remove_duplicates(some_list):
    withot_duplicates = []
    for element in some_list:
        if element not in withot_duplicates: # Si el elemento no esta en withot_duplicates
            withot_duplicates.append(element)
    return withot_duplicates


def run():
    random_list = [1,1,1,2,2,3,3,4]
    print(remove_duplicates(random_list))

if __name__ == "__main__":
    run()