# A common use case of context managers is locking
# and unlocking resources and closing opened files
from contextlib import contextmanager

class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        return self.file_obj.close()
        

# by defining the enter and exit methods, we can use a class in a with statement

with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')

# What happens under the hood
# The with statement stores the __exit__ method of the File class.
# It calls the __enter__ method of the File class.
# The __enter__ method opens the file and returns it.
# The opened file handle is passed to opened_file.
# We write to the file using .write().
# The with statement calls the stored __exit__ method.
# The __exit__ method closes the file.


# this is more or less like what we do in file I/O
with open('demo.txt', 'r') as opened_file:
    lines = [line.split('\n') for line in opened_file]
    print(len(lines))


@contextmanager
def open_file(filename, mode='r'):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

with open_file('demo.txt', 'a') as f:
    f.write("\nHello, Babe!")