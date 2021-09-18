
# Positive integers are the numbers 1, 2, 3,
# sometimes called the counting numbers or natural numbers

# Sources:
# https://snakify.org/en/lessons/if_then_else_conditions/
# https://stackoverflow.com/questions/26198131/check-if-input-is-positive-integer
# https://github.com/HenkT28/pands-problem-set/blob/master/collatz.py
# http://www.trytoprogram.com/python-programming/python-while-loop/
# https://stackoverflow.com/questions/20372485/what-does-end-exactly-do

# The while loop contains a boolean expression and the code inside the loop
# is repeatedly executed as long as the boolean expression is true.

# The ValueError: Raised when a built-in operation or function receives 
# an argument that has the right type but an inappropriate value

# This program is to prevent the user entering
# a negative integer or non integer
goodinput = False
while not goodinput:
    try:
        number = int(input('Please enter a postive integer: '))
        if number > 0:
            goodinput = True
            print("The answer is:")
        else:
            print("That's not a positive integer. Try again: ")
    except ValueError:
        print("That's not an integer. Try again: ")
# This section of code executes if the number entered is a positive integer
else:
    while number != 1:
        print(number, end =' ')
        if number % 2 == 0:
            number = number // 2
        else:
            #number is odd
            number = number * 3 + 1
    else:
        print(number, end =' ')