"""4: Inputs"""

# Sometimes you might want to ask the user a question. To do that, we use
# a special function called `input`. Functions are covered in `5-functions.py`.
# You can ignore the # pylint comment, it is there to tell tools which analyze
# the code that in fact everything is OK with this line.

days = 365  # pylint: disable=C0103
print('there are ' + str(days) + 'in a normal year')

days = int(input('How many days in a leap year? '))  # pylint: disable=C0103
if days == 366:
    print('Well Done!')
else:
    print('(Its one more than every other year)')

# Try running the above code, and type in your answer.
# What happens if you try to type a letter instead of a number? Try it now and
# come back

# You should get an ValueError saying that you gave an invalid literal for
# int() This is because we use a thing which is called a cast. By default,
# input gives us a string, but we cannot compare string to an int, so we need
# to convert it to an a number - int.
