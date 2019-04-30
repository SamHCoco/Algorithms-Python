# Algorithms: Python Implementations
Implementation of various classes of algorithms (e.g. search or sort) in Python.

# Introduction
An algorithm can be defined as a series of steps used to produce some result. They have a specific meaning in computer science and are defined by the following **3 characteristics**:
 * *They are finite: algorithms must terminate after a finite number of steps.*
 * *Algorithms operate on data.*
 * *They must produce at least one result as output.*

# Sorting Algorithms
*  ## Bubble Sort
 ```Python
 def bubble_sort(number_list):
     """Sorts list of numbers into ascending order using bubble sort algorithm.

     args:
     number_list (list) -- a list of real numbers

     returns: The number list sorted in ascending order or null if the list
     is has less than 2 elements, or contains a non-numeric element.
     """
     list_size = len(number_list)
     if list_size < 2:
         print("ERROR: list must contain at least 2 number or more")
         return None

     for element in number_list:
         if type(element) not in (int, float):
             print("ERROR: list contains non-numerical object '{}'".format(element))
             return None
     i = 0
     is_sorted = False
     swaps_counter = 0
     while not is_sorted:
         while i != list_size - 1:
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
     return number_list
 ```
# Searching Algorithms
*  ## Binary Search
```Python
def binary_search(search_value, numbers_list):
    """Searches for number in list using binary search.

    args:
    search_value (real number) - the search value to find in list
    numbers_list (list) - list to be searched to find specified value

    returns: The index of the searched value, None if not found or input is invalid
    """
    if is_valid_input(numbers_list, "BINARY SEARCH") is False:
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
            print("BINARY SEARCH: {} not found".format(search_value))
            return None
        if numbers_list[middle_index] == search_value:
            found = True
        elif search_value > numbers_list[middle_index]:
            first_index = middle_index
        elif search_value < numbers_list[middle_index]:
            last_index = middle_index
    print("BINARY SEARCH: {} found at index {}".format(search_value, middle_index))
    return middle_index
```
