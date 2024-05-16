# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes":
           return "yes"
        elif response == "y" :
            return "yes"
        elif response == "no":
            return "no"
        elif response == "n" :
            return "no"
        else:
            print("Please enter yes / no")

# Displays instructions to user
def instruction():
    print('''
    
**** Instructions ****
    
To begin, decide on a score goal (eg: The first one to get a 
score of 50 wins).

For each round of the game, you win points by rolling dice.
The winner of the round is the one who gets 13 (or slightly less).

If you win the round, then your score will increase by the
number of points that you earned. If your first roll of two 
dice is  double (eg: both dice show a three), then your score
will be DOUBLE the number of points.

If you lose the round, then you don't get any points.

If you and the computer tie (eg: you both get a score of 11,
then you will have 11 points added to your score
    
    ''')

#Checks that users enter an integer
# that is more than 13
def int_check():

    while True:

        error = "Please enter an integer that is 13 or more"

        try:
            response = int(input("Ener an integer: "))

            # checks that the number is more than / equal to 13
            if response < 13:
                print(error)
            else:
               return response

        except ValueError:
            print(error)

# Main routine
print()
print("🎲🎲 Roll It 13! 🎲🎲")
print()

want_instructions = yes_no("Do you want to read the instructions?") . lower()

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
   instruction()

print()
target_score = int_check()