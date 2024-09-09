###
# Välja ett tal

correctNumber = 6
numOfGuesses = 3

# Be om en siffra

while (numOfGuesses > 0):
    print("guess a number")
    guess = int(input())
    #print("you guessed") 
    #print(guess)

    numOfGuesses -= 1
    # Kolla om siffran är större

    if (guess > correctNumber):
        print("you guessed to large. Try again.")
        #, mindre eller lika    
    elif (guess < correctNumber):
        print("you guessed to small. Try again.")
    else:
        print("you guessed correct")
        numOfGuesses = 0

    

# göra tre gånger

