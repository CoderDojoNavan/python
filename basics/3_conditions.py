"""3: Conditions"""

# Sometimes you want to check is one variable the same as other, or maybe
# if a number is bigger or smaller than another number. For that we use
# what is called conditional statements. Remember you can only compare
# variables of the same type (like int, or string)

age: int = 10

print('the age is {}'.format(age))

if age < 18:
    print('you are a child')

# But what is we want to show that someone is still a child? We could do

if age < 18:
    print('you are a child')
if age > 18:
    print('you are an adult')

# But another way to do it is

if age < 18:
    print('you are a child')
else:
    print('you are an adult')
