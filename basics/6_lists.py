"""6. Lists"""

# Sidenote: You can ignore the comment # pylint: disable=C0103,
#           this is because we are not writing full python projects yet!

# Sometimes you need to store a few names or numbers. We can do it in a data
# structure called list (also known as arrays). This is an example of a list:

names = ['Alice', 'Bob', 'Charlie']  # pylint: disable=C0103

# We use the square brackets to create a list. When naming a list, we usually
# use the plural of the word.

numbers = [1, 2, 3, 4, 5]  # pylint: disable=C0103

# We can store any sort of data type in a list, but they must be the same.
# Python will not complain if you do mix them, but it will make your program
# very slow and you can have bugs.

# We can print a list to show its elements

print(names)
print(numbers)

# Sometimes we want to just get a single value from a list. To do that, we can
# use something called an index. Every element in a list has its index - they
# are numbers, and they are being counted from 0. We can get a value by also
# using the square brackets. Above we defined names list, now we will print
# the first value in the list:

first_name = names[0]  # pylint: disable=C0103

print(first_name)

# Remember, its easy to accidentally get over the maximum index. If we get the
# 5th value, it will fail, as names list contains only 3 elements:

# print(names[4])

# (Remember, 5th element has index of 4 - we are counting from 0.).
# If you remove the # from the beginning of the line you should see an
# `IndexError`.

# From time to time, we might also want to change a value in the list, to do
# that we also use indexes

print(names)

names[2] = 'Caroline'

print(names)

# You should see that the last name in the names list changed to Caroline.

# You can always extend your array, by adding additional name.

names.append('Dennis')

print(names)

# If you want to remove a name from the list, you can use the `del` keyword.

del names[0]

print(names)

# You should see that the first name is gone!

# Sometimes you want to check how long a list is, you can do that using
# len() function, which takes in the list, and returns its length.

print('There are ' + str(len(names)) + ' names in the name array')

# If you want to check is a specific value in a list, you can use the `in`
# keyword in your if statements.

wanted_name: str = 'Alice'
if wanted_name in names:
    print(wanted_name + ' is in names list')
else:
    print(wanted_name + ' is not in the names list')
