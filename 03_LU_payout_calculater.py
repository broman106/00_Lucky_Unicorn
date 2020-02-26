# Lucky Unicorn Decomposition step 3
# Generate a random token

# to do
# Set up starting amount
# Choose 100 tokens (ie: play 100 rounds and ...
# count # of unicorns and multiply by 5
# count # of horse / zebra and multiply by 0.5
# count # of donkey
# work out total won / lost

import random

HOW_MUCH = 100
tokens = ["horse","horse","horse",
          "zebra", "zebra","zebra",
          "donkey", "donkey","donkey","unicorn"]

unicorn_count = 0
zebhor_count = 0
donkey_count = 0

for item in range (0,HOW_MUCH):

    chosen = random.choice(tokens)

    if chosen == "unicorn":
        unicorn_count+= 1
    elif chosen== "donkey":
        donkey_count += 1
    else:
        zebhor_count += 1

    print(chosen)

# Money calculation ...
winnings = unicorn_count * 5 +zebhor_count * 0.5

print("**** win / loss calculation*****")
print("# Unicorns: {}".format(unicorn_count))
print("# zebra / horses: {}".format(zebhor_count))
print ("# Donkey: {}".format(donkey_count))

print()
print("you spent ${}".format(HOW_MUCH))
print("you go home with ${:.2f}".format(winnings))