"""
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers.
No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
[10, 343445353, 3453445, 3453545353453] should return 3453455.
"""

def sum_of_two_smallest_numbers(start: list) -> int:

#    start = [1, 10, 100, 120, 130, 140, 2]
#    spisok_new = []

#    for char in start:
#       if char < 0 or isinstance(char, int) == False:
#            return "Числа в списке должны быть положительными и целыми!"
#       else:
#            # spisok_new.append(char) #None - ?
#           spisok_sorted = sorted(spisok_new.append(char))
#
#            return spisok_sorted
    sorted_start = sorted(start, reverse=False)
    sum_of_nums = sorted_start[0] + sorted_start[1]

print(sum_of_two_smallest_numbers([1, 10, 100, 120, 130, 140, 2]))