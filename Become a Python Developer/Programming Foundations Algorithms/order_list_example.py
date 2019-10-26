# searching for an item in an ordered list
# this technique uses a binary search


items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]


def binary_search(item, item_list):
    # get the list size
    list_size = len(item_list) - 1
    # start the two ends of the list
    lower_index = 0
    upper_index = list_size

    while lower_index <= upper_index:
        # calculate the middle point
        mid_point = (lower_index + upper_index) // 2
        # if item is found, return the index
        if item_list[mid_point] == item:
            return mid_point
        # otherwise get the next midpoint
        if item > item_list[mid_point]:
            lower_index = mid_point + 1
        else:
            upper_index = mid_point - 1

    if lower_index > upper_index:
        return None


print("Position: ", binary_search(23, items))
print("Position: ", binary_search(87, items))
print("Position: ", binary_search(250, items))