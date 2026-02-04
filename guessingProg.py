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

winning_number = 65
won = []

win = int(input("Guess any number: "))
won.append (win)

if (won == winning_number):
    print("YOU WINN!!!!")
    if (won < winning_number):
        print ("Number too low.")
    else :
        print ("Number too high.")

else:
    print ("Try again!")