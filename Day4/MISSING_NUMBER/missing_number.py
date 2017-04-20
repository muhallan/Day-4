def find_missing(first_list, second_list):
    """ a function that returns the extra number missing in one of the two positive integer arrays passed """
    if first_list == [] or second_list == []:
        return 0

    if first_list == second_list:
        return 0

    missing_number = []

    larger_list = first_list if len(first_list) > len(second_list) else second_list
    smaller_list = first_list if len(first_list) < len(second_list) else second_list
    for number in larger_list:
        if number not in smaller_list:
            missing_number.append(number)
    return missing_number[0]
