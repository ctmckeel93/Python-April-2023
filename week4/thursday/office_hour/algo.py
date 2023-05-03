# Your goal is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.

# array_diff([1,2],[1]) == [2]
# If a value in 'a' is present in b, all of its occurrences must be removed from the other:

# array_diff([1,2,2,2,3],[2]) == [1,3]

# No morphing
def array_diff(list1, list_diff):
    if not len(list_diff): return 

    new_list = []
    for entry in list1:
        if not entry in list_diff:
            new_list.append(entry)

    return new_list

# in place
def array_diff2(list1, list_diff):
    print("running once")
    if not len(list_diff): return list1

    for i in range(len(list1)):
        print(i)
        if list1[i] in list_diff:
            print(list1[i])
            list1.pop(i)
            print(list1)
            return array_diff2(list1,list_diff)


    return 0 

result1 = array_diff([1,2,2,2,3],[2])
print(result1)
array = [1,2,2,2,3]
array_diff2(array, [])
print(array)


