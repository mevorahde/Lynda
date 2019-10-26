# determine if a list is sorted

items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def is_sorted(item_list: list):
    # using the brute force method
    #for i in range(0, len(item_list) - 1):
        #if item_list[i] > item_list[i + 1]:
            #return False

    # alternative way using Python's 'all' function
    return all(item_list[i] <= item_list[i+1] for i in range(len(item_list) - 1))

    return True


print("This list is sorted: ", is_sorted(items1))
print("This list is sorted: ", is_sorted(items2))
