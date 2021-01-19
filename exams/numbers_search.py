def numbers_searching(*args):

    all_numbers = []
    duplicates = set()

    minimum_num = min(args)
    maximum_num = max(args)
    sum_of_potential_nums = sum(range(minimum_num, maximum_num + 1))

    for number in args:
        if number in all_numbers:
            duplicates.add(number)
        else:
            all_numbers.append(number)

    difference = sum_of_potential_nums - sum(set(all_numbers))

    result = [difference, list(sorted(duplicates))]

    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))





#   1    2    3    5    6

 #    if next_number - previous_number != 1 -> togava lipsva chisloto