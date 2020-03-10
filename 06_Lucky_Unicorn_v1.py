# Lucky unicorn Fully working program
# program should work - needs to be tested for usability

import random

# Integer checking function below
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

# main routine goes here

# Ask user how much they want to play with (min $1, max $10)
balance = intcheck("how much money would you like to play with? ", 1, 10)

# tokens list includes 10 times to items to prevent too many unicorns being chosen
tokens = ["horse","horse","horse",
          "zebra", "zebra","zebra",
          "donkey", "donkey","donkey","unicorn"]

# Randomly choose a token from our lits above
token = random.choice(tokens)
print()
print("you got a {}".format(token))

# Adjust balance correctly for a given token
if token == " unicorn":
    balance += 5
    feedback = "congratulations oyu won $5.00"
elif token == "donkey":
    balance -= 1
    feedback = "sorry, you did not win anything this round"
else:
    balance -= 0.5
    feedback = "congratulations you won 50c"

print()

print(feedback)
print("You have ${:.2f} left".format(balance))

if balance < 1:
    print("Sorry you don't have enough money to continue. game over")
    keep_going = "end"
else:
  keep_going = input("Press <enter> to play again or any key to quit")

print("Thank you for playing.")