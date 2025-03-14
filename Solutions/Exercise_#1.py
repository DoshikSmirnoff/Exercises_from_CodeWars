"""
Your task is to make a function that can take any non-negative integer as an argument
and return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number.

Examples:

Input: 42145 Output: 54421
Input: 145263 Output: 654321
Input: 123456789 Output: 987654321
"""
def descending_order(num: str) -> int:
    if len(num) < 2:
        print("Введите число, состоящее из более чем одной цифры!")
    else:
        num_sorted_list = sorted(list(num), reverse=True)
        new_num = ""
        for char in num_sorted_list:
            new_num += char

        num_result = int(new_num)

        print(num_result)

descending_order(input("Введите число, состоящее не менее чем из 2х цифр: "))