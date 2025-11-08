# Reading Large Files
def csv_reader(filename):
    with open(filename, 'r') as file:
        for row in file:
            yield row

csv_gen = csv_reader("C:/Users/Billy/Downloads/techcrunch.csv")

row_count = 0
for row in csv_gen:
    row_count +=1
print(f"Row count is {row_count}")

# Generating an infinite sequence
def infinite_sequence():
    num = 0
    while num <= 20: # you could put while True:
        yield num
        num+=1

for i in infinite_sequence():  
        print(i, end=' ')

# Detecting Palindromes
def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False
# Borrowing logic from the generating an infinite sequence example
def infinite_sequence():
    num = 0
    while num <10000: # you could put while True:
        yield num
        num+=1
for x in infinite_sequence():
    pal = is_palindrome(x)
    if pal:
        print(x)

# PROFILING GENERATOR PERFORMANCE
import sys
nums_squared_lc = [i**2 for i in range(100000)] # List Comprehension
print(f"List comprehensions: {sys.getsizeof(nums_squared_lc)} size in memory")
nums_squared_gc = (i**2 for i in range(100000))# Generator Expression
print(f"Generator comprehensions: {sys.getsizeof(nums_squared_gc)} size in memory")
# Note that list comprehensions are faster to compute than generators. Therefore is speed and not memory
# is of essence, consider using a list instead of a generator
