# Variables are used to store information later on, if you want to listen
# to what the user wants to say or keep something as a result.
# There are various types of variables, but the most basic ones are:
#   int - a whole number, like 5
#   float - a real number, like 3.14
#   str - a string (a series of characters), like 'hello'
#   bool - yes or no, True or False

# Once you create a variable, you MUST NEVER assign it a value of another type:
# a = 5
# a = 'hello' <----- NEVER DO THIS.

# Below you can see a couple of variables being created, together with the
# optional types added. They can be ommitted.

a: int = 5
b: float = 3.14
c: str = 'hello'
d: bool = True

print(a)
print(b)
print(c)
print(d)


# You can name the variables however you want (in most cases). They should make
# sense, so try to describe them. If you have nice variables, the code is easy
# to read. There is no need to have long names, but they shouldn't be too short
# either

wall_colour: str = 'yellow'

print('The wall is ' + wall_colour)
