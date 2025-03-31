"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with
all of the integer's divisors(except for 1 and the number itself), from smallest to largest.
If the number is prime return the string '(integer) is prime'.

Examples:

divisors(12) --> [2, 3, 4, 6]
divisors(25) --> [5]
divisors(13) --> "13 is prime"
"""

def divisors(start_num: int) -> list or str:
    result = []

    for i in range(2, start_num // 2 + 1):
        if start_num % i == 0:
            result.append(i)

    if len(result) == 0:
        return f"{start_num} is prime"
    else:
        return result

print(divisors(24))