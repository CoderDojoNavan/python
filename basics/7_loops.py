"""7: Loops"""

# Another very important topic in any programming language. It allows to go
# over every element in an array. There are two types of loops: for loops,
# and while loops.

# Sidenote: You can ignore the comment # pylint: disable=C0103,
#           this is because we are not writing full python projects yet!

##############################################################################

# For loops: The way to do it, it using the `in` keyword.

for word in ['every', 'word', 'in', 'array']:
    print(word)

# Going element by element in array is called iterating - in the above case we
# iterated through every world in the array ['every', 'word', 'in', 'array']
# and then printed it. We can also iterate over any variable type:


print('Iterating over a string')
for letter in 'string':
    print(letter)

print('Iterating over numbers (primes)')
for number in [2, 3, 5, 7, 11, 13, 17, 19]:
    print(number)

print('Iterating over a generated range of numbers')
for number in range(10):
    print(number)

# The range() function shown above, generates a list of numbers, up to the
# number you provide it.

##############################################################################

# While loops:

# While loops keep on running when a condition is being satisfied. Think of it
# as `if` statement combined with a `for` loop:

a = 0  # pylint: disable=C0103
while a < 10:
    print('Still going...')
    a += 1
print('We are out of the loop')

# We can also have an infinite loop, and only exit out of the loop,
# (also called breaking out of the loop), by using the `break` keyword

while True:
    value = input('Type q to exit: ')  # pylint: disable=C0103
    if value == 'q':
        break
    print('You typed ' + value + '. We are not out of the loop yet')
print('now we are out!')

##############################################################################

# Ok. But what can we do with loops? A lot!

numbers = [17, 2, 3, 5, 11, 19, 13, 7]  # pylint: disable=C0103

total = 0  # pylint: disable=C0103
for n in numbers:
    total += n
print(total)

largest = numbers[0]  # pylint: disable=C0103
for n in numbers:
    if n > largest:
        largest = n

print('largest number in the list is ' + str(largest))
