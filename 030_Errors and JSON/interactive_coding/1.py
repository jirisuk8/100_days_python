fruits = ["Apple", "Pear", "Orange"]

# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError as e:
        print(f"List does not have this many items, {e}")
        print("Fruit pie")

make_pie(2)