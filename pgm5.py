def have_common_member(list1, list2):
    return bool(set(list1) & set(list2))

list1 = [1, 2, 3, 4]
list2 = [5, 6, 3, 7]
print("Have common member?", have_common_member(list1, list2))

list3 = [8, 9]
print("Have common member?", have_common_member(list1, list3))
