# Asks the user to enter a postive floating-point number.
# Creates a function to calculate an approximation of 
# it's square root using Newton's Method. Runs Newtons Method
# over and over until we get closest approximation.

def newton_sqrt(number, tolerance):
    x = number
    iterations = 0
    while True:
        iterations += 1
        sqrt = 0.5 * (x + (number / x))
        if (abs(sqrt - x) < tolerance):
            break
        x = sqrt
    return sqrt

def main():
    x = 0
    while True:
        try:
            x = float(input("Please enter a positive number: "))
            if (x < 0):
                raise ValueError
            print("The square root of " + str(x) + " is approximately ", str('%.2f' % newton_sqrt(x, 0.001)))
           
        except ValueError:
            print("This number is invalid. Please try again.")
if __name__ == "__main__" :
    main()
