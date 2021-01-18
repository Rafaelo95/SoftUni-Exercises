def list_manipulator(list_of_nums, *args):

    list_to_modify = list_of_nums
    second_parameter = args[0]
    third_parameter = args[1]
    has_number = True

    if second_parameter == "add":
        numbers = args[2:]
        if third_parameter == "beginning":
            list_to_modify = [*numbers] + list_to_modify

        elif third_parameter == "end":
            list_to_modify = list_to_modify + [*numbers]

    elif second_parameter == "remove":

        try:
            number = args[2]
        except IndexError:
            has_number = False

        if third_parameter == "beginning":

            if has_number:
                number = args[2]
                list_to_modify = list_to_modify[number:]
            else:
                list_to_modify = list_to_modify[1:]

        elif third_parameter == "end":
            if has_number:
                number = args[2]
                list_to_modify = list_to_modify[:number - 1]
            else:
                list_to_modify = list_to_modify[:-1]

    return list_to_modify


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
