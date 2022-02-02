import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


def say_greeting():
    print("How are you")


decorated_function = delay_decorator(say_greeting)
decorated_function()

# say_hello()
# say_greeting()


# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args}")
        print(f"It returned {function(args[0], args[1], args[2])}")
    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
    return a + b + c

a_function(1,2,3)