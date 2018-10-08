# With functions we can combine multiple instructions into a single block and
# use it again in the future. You already were using functions, do you remember
# what they were called?

# A function is created using the `def` keyword, with the name of the function
# after it.


def printHello():
    print('hello!')

# We can then call the function


printHello()
printHello()

# You should see the word `hello` twice. We can also pass some value to the
# function by giving it arguments.


def addAndPrint(a: int, b: int):
    result = a + b
    print(str(a) + ' + ' + str(b) + ' = ' + str(result))

# In the previous `printHello` example we just had empty brackets after the
# function name when we were calling it. This time, the function wants two
# arguments, a and b, and both of them are ints. Again, the types are optional.


addAndPrint(4, 5)

# We can also return a variable from a function by using the `return` keyword.
# We can also optionally specify the type of the variable that will be returned
# from the function using `-> type`


def add(a: int, b: int) -> int:
    return a + b

# Because we return a value, python doesn't know what to do with it. So we will
# just print it.


result = add(6, 7)
print(result)

# We are creating a new variable result here, but since we will not use it any
# where else, we can just put a command inside another command (print):

print(add(8, 9))

# Do you rememember that from `4-inputs.py`?
