def new_merge_lists(list1, list2):
    merged_list = []

    while list1 and list2:
        if list1[0] <= list2[0]:
            merged_list.append(list1[0])
            list1 = list1[1:]
        else:
            merged_list.append(list2[0])
            list2 = list2[1:]

    if list1:
        merged_list += list1
    if list2:
        merged_list += list2

    return merged_list

# Test
list1 = [1, 3, 10]
list2 = [0, 4, 7, 9]
result = new_merge_lists(list1, list2)
print("Merge List (Test):", result)

