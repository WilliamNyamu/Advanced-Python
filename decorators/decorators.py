import functools #preserves information about the original function

def do_twice(func):
    @functools.wraps(func) 
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def say_whee():
    print("Whee!")
say_whee()

@do_twice
def greet(name):
    print(f"Hello {name}")

greet("babe")

print("Showing the documentation for defined functions: ")
print(say_whee)

print(say_whee.__name__)

print(help(say_whee))