def remove_duplicates(list):
    my_set = set(list)
    return my_set


def run():
    random_list = [1,2,1,3,1,5,6,7,6,4,1,2,3,9,8,2,3,5,9,8,4,2,1,4,5,2]
    my_set = remove_duplicates(random_list)
    print(my_set)

if __name__ == "__main__":
    run()