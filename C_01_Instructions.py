print("🎲🎲 Roll It 13! 🎲🎲")


# loop for testing purposes

while True:
    want_instructions = input("Do you want to read the instructions?") . lower()

# checks users enter yes (y) or no (n)
    if want_instructions == "yes":
        print ("you chose yes")
    elif want_instructions == "y" :
        print("you chose yes")
    elif want_instructions == "no":
        print("you chose no")
    elif want_instructions == "n" :
        print("you chose no")
    else:
        print("You did not choose a valid response")