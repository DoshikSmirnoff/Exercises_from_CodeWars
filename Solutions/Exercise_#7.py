"""
Give you a number array numbers and a number c.

Find out a pair of numbers(we called them number a and number b) from the array numbers,
let a*b=c, result format is an array [a,b]

The array numbers is a sorted array, value range: -100...100

The result will be the first pair of numbers, for example,findAB([1,2,3,4,5,6],6) should return [1,6],
instead of [2,3]

Please see more example in testcases.
"""
def find_a_b_var1(numbers, c):

    for i, a in enumerate(numbers, 1):
        for b in numbers[i:]:
            if a * b == c:
                return [a, b]

    return None

def find_a_b_var2(numbers, c):

        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if numbers[i] * numbers[j] == c:
                    return [numbers[i], numbers[j]]

        return None