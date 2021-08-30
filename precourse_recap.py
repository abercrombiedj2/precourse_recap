# A simple game to guess the number of days to Christmas using an if-else statement.
correct = "117"
guess = input("Can you guess how many days until Christmas? ")

if guess == correct:
    print("Correct! It is %s days until Christmas!" % correct)
else:
    print("Nope! You're way off.. no presents for you!")