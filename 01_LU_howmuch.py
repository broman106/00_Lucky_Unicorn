# Ask user for number
# Loop question so that ti repeats until valid number is entered
# make code recyclable!

# Integer checking function
def intcheck(question, low, high):
    valid = False
    error = "please enter an integer between {} and {}".format(low, high)
    while not valid:
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
keep_going =""
while keep_going == "":
    how_much = intcheck("how much money do you want to play with ", 1, 15)
    print("You have chosen to play with ${}".format(how_much))

    keep_going = input("Again? ")