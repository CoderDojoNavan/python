"""5: Functions"""

# With functions we can combine multiple instructions into a single block and
# use it again in the future. You already were using functions, do you remember
# what they were called?

# A function is created using the `def` keyword, with the name of the function
# after it.


def print_hello():
    """Simply prints hello"""
    print('hello!')

# Notice the special """ - it is a function comment, which allows the code
# to be better understood by special tools which analyse code and spot mistakes
# as well as generated documentation. We can now call the function:


print_hello()
print_hello()

# You should see the word `hello` twice. We can also pass some value to the
# function by giving it arguments.


def add_and_print(num1: int, num2: int):
    """Adds two numbers together and prints the results"""
    print(str(num1) + ' + ' + str(num2) + ' = ' + str(num1 + num2))

# In the previous `printHello` example we just had empty brackets after the
# function name when we were calling it. This time, the function wants two
# arguments, a and b, and both of them are ints. Again, the types are optional.


add_and_print(4, 5)

# We can also return a variable from a function by using the `return` keyword.
# We can also optionally specify the type of the variable that will be returned
# from the function using `-> type`


def add(num1: int, num2: int) -> int:
    """Adds two numbers together and returns the result"""
    return num1 + num2

# Because we return a value, python doesn't know what to do with it. So we will
# just print it. You can ignore the # pylint comment - the code here is only
# for demonstrative purposes, and the tool which checks is everything ok with
# the code doesn't like the fact we assign a variable and never use it again


result = add(6, 7)  # pylint: disable=C0103
print(result)

# We are creating a new variable result here, but since we will not use it any
# where else, we can just put a command inside another command (print):

print(add(8, 9))

# Do you rememember that from `4-inputs.py`?
