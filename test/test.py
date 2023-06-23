import numpy as np
scan_a = input("Enter First digit: ")
scan_b = input("Enter second digit: ")


def myfunc(num1, num2):
    if num1*num2 <= 1000:
        return num1 * num2
    else:
        return num1 + num2
    
my_string = "The result is {}"
print(my_string.format(myfunc(int(scan_a), int(scan_b))))

