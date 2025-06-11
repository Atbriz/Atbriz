import random

keep_playng = "yes"
while keep_playng == "yes":   
    
    
    secret_number = random.randint(1, 100)
    guess_count = 0

    guess = -2
    while guess != secret_number:
        guess = int(input(" What is your guess? "))
        guess_count = guess_count + 1
        
        if guess < secret_number:
            print("Higher")
        elif guess > secret_number:
            print("Lower")
        else:
            print("You guessed it ")
            
    print (f"it took you {guess_count} guesses ")   

    keep_playng = input ("Would you like to play agin (yes/no)")     
            
            
