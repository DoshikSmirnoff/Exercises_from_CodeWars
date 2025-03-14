"""
Given an integral number, determine if it's a square number:
In mathematics, a square number or perfect square is an integer that is the square of an integer;
in other words, it is the product of some integer with itself.
The tests will always use some integral number,
so don't worry about that in dynamic typed languages.

Examples

-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false
"""

import math

def square_numbers(num: int) -> bool:

    if num > 0:
        if num == math.sqrt(num)**2:
            return True
        else:
            return False
    else:
        return False

print(square_numbers(int(input("Введите целое число: "))))