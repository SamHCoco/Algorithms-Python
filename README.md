# Algorithms: Python Implementations
Implementation of various classes of algorithms (e.g. search or sort) in Python.
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
