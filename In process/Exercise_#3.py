"""
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers.
No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
[10, 343445353, 3453445, 3453545353453] should return 3453455.
"""

def sum_of_two_smallest_numbers(start_list: list) -> list:
    #start_list = [1, 10, 100, 120, 130, 140, 2]
    spisok_new = []

    for char in start_list:
        if char < 0 or isinstance(char, int) == False:
            print("Числа в списке должны быть положительными и целыми!")
        else:
            spisok_new += char
            spisok_sorted = sorted(spisok_new)

    print(spisok_sorted)


sum_of_two_smallest_numbers(start_list = [1, 10, 100, 120, 130, 140, 2]) # TypeError: 'int' object is not iterable