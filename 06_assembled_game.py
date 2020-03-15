# lucky unicorn - end mechanics

# To do
# Ask user how much money they have to play with
#If the total is more than $1, quit
# If the total is more than $1, ask user if they want to keep going
import random


def statement_decorator(statement, decoration):
    print(decoration * len(statement))
    print(statement)
    print(decoration * len(statement))


# Integer checking function
def intcheck(question, low, high):
    valid = False
    error = "please enter an integer between {} and {}".format(low, high)
    while not valid:
        try:
            response = int(input(question))

            if low <= response <= high:
                 return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# Main Routine starts here

tokens = ["horse","horse","horse",
          "zebra", "zebra","zebra",
          "donkey", "donkey","doneky", "unicorn",]

# Assume starting amount is $10
total = intcheck("How much would you like to play with? ", 1, 10)

keep_going = ""
while keep_going == "":

    # Allow manual token input for testing purposes
    token= random.choice(tokens)

    # Adjust total correctly for a given token
    if token == "unicorn":
        total += 5
        feedback = "*** Yay a unicorn , and you won $5.00 ****"
        symbol = "*"
    elif token == "donkey":
        total -= 1
        feedback = "!!! Sorry, you got a donkey and got nothing !!!"
        symbol = "!"
    else:
        total -= 0.5
        feedback = "^^^^ Congratulations you got a {} and won 50c ^^^^".format(token)
        symbol = "^"

    print()

    statement_decorator(feedback, symbol)
    print("You have ${:.2f} to play with".format(total))

    if total < 1:
        statement_decorator("!! Sorry you lose !!", "!",)
        print()
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit")

    print("Thank you for playing.")

