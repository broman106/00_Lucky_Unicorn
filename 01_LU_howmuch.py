# Ask user for number
# Loop question so that ti repeats until valid number is entered
# make code recyclable!

# Integer checking function
def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "whoops! please enter an integer between {} and {}".format(low, high)

        try:
            response = int(input("Enter an integer between {} and {}: ".format(low, high)))

            if low <= response <= high:
                 return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# main routine goes here

how_much = intcheck("how mu money do you want to play with ", 1, 15)