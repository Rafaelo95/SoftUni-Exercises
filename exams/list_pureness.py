from collections import deque

def best_list_pureness(list, number):

    list_to_modify = deque(list)
    rotation_and_value = {}
    result = 0

    for item, index in enumerate(list_to_modify):
        result += (item * index)
        rotation_and_value[0] = result

    result = 0

    for i in range(1, number + 1):

        last_element = list_to_modify.pop()
        list_to_modify.appendleft(last_element)

        for item, index in enumerate(list_to_modify):
            result += (item * index)

        rotation_and_value[i] = result

        result = 0

    pureness_value = 0
    count_rotations = 0

    for key, value in rotation_and_value.items():
        if value > pureness_value:
            pureness_value = value
            count_rotations = key

    return f"Best pureness {pureness_value} after {count_rotations} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
