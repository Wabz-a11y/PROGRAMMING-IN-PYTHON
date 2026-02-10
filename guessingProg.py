"""
Exercise "NUMBER GUESSING GAME"
Make a variable, like winning_number and assign any number to it.
Ask user to guess a number.
If user guessed correctly then print "YOU WIN!!!!"
If user didn't guessed correctly then: 
     If user guessed lower than actual number the print "too low"
     If user guessed higher than actual number then print "too high"

bonus
g

"""
"""

winning_number = 65

guess = int(input("Guess any number: "))

if guess == winning_number:
    print("YOU WIN!!!!")
elif guess < winning_number:
    print("Too low")
else:
    print("Too high")

"""

winning_number = 65

while True:
    guess = int(input("Guess any number: "))

    if guess == winning_number:
        print("YOU WIN!!!!")
        break
    elif guess < winning_number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
