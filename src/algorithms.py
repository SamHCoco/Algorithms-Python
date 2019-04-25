def list_size(list_input):
    """Calculates the size of the inputted list.

    returns: The number of element in the inputted list
    """
    return len(list_input)


def is_valid_input(list_input, algorithm_name):
    """Validates that input given is a list that contains only numbers.

    args:
    list_input (list) -- the list to be validated
    algorithm_name -- the algorithm calling on this method for validation

    returns: None if the input contains a non-numeric object
    """
    for element in list_input:
        if type(element) not in (int, float):
            print("{} ERROR: list contains non-numerical object '{}'".format(algorithm_name, element))
            return False
    if list_size(list_input) == 0:
        print("{} ERROR: number list is empty".format(algorithm_name))
        return False
    return True

# ******************************** SORTING ALGORITHMS **************************************************


def bubble_sort(number_list):
    """Sorts list of numbers into ascending order using bubble sort algorithm.

    args:
    number_list (list) -- a list of real numbers

    returns: The number list sorted in ascending order or null if the list
    is has less than 2 elements, or contains a non-numeric element
    """
    size = list_size(number_list)
    if size < 2:
        print("ERROR: list must contain at least 2 number or more")
        return None
    if is_valid_input(number_list, "BUBBLE SORT") is False:
        return None
    i = 0
    is_sorted = False
    swaps_counter = 0
    while not is_sorted:
        while i != size - 1:
            if number_list[i] < number_list[i + 1]:
                i += 1
            elif number_list[i] > number_list[i + 1]:
                higher = number_list[i]
                lower = number_list[i + 1]
                number_list[i] = lower
                number_list[i + 1] = higher
                swaps_counter += 1
                i += 1
            elif number_list[i] == number_list[i + 1]:
                i += 1
        if swaps_counter == 0:
            is_sorted = True
        else:
            swaps_counter = 0
            i = 0
    print("BUBBLE SORT RESULT: {}".format(number_list))
    return number_list

# ********************************* SEARCHING ALGORITHMS **************************************


def bisection_search(search_value, numbers_list):
    """Searches for number in list using bisection search.

    args:
    search_value (real number) - the search value to find in list
    numbers_list (list) - list to be searched to find specified value

    returns: The index of the searched value, None if not found or input is invalid
    """
    if is_valid_input(numbers_list, "BISECTION SEARCH") is False:
        return None
    numbers_list = sorted(numbers_list)
    print("BINARY SEARCH - SORTED LIST: {}".format(numbers_list))
    first_index = 0
    last_index = list_size(numbers_list) - 1
    middle_index = None
    found = False
    while not found:
        middle_index = (first_index + last_index) // 2
        if middle_index == first_index:
            print("BISECTION SEARCH: {} not found".format(search_value))
            return None
        if numbers_list[middle_index] == search_value:
            found = True
        elif search_value > numbers_list[middle_index]:
            first_index = middle_index
        elif search_value < numbers_list[middle_index]:
            last_index = middle_index
    print("BISECTION SEARCH: {} found at index {}".format(search_value, middle_index))
    return middle_index
