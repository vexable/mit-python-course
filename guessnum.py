high = 100
low = 0
print("Please think of a number between 0 and 100")
guess = (high+low)//2
while True:
    print("Is your secret number " + str(guess) + "?")
    response = str(input( "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly "))
    if response.lower() == "h":
        high = guess
        guess = (high+low)//2
    elif response.lower() == "l":
        low = guess
        guess = (high+low)//2
    elif response.lower() == "c":
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")