def add(*args):
   return print(sum([i for i in args]))

add(35, 6, 8, 2)

def calculate(n, **kwargs):
    n += kwargs["add"]
    n*= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)