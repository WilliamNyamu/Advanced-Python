# Create a Boolean-Valued function(predicate function) for checking whether a given number is prime or not
import math

def is_prime(number):
    if number < 1:
        return False
    for i in range(2, int(number)):
        if number % i == 0:
            return False
    return True