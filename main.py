import random
num = random.randint(1 , 10)



tries = 0

while (True):
    guess = int(input("Guess a number between 1 to 10 : "))


    if (num == guess):
        tries += 1
        print(f"You are right and you guessed the number in {tries} try!!")
        break
    
    elif (num < guess):
        print("You have to go little lower!!")
        tries += 1
    
    elif (num > guess):
        print("You have to go little higher!!")
        tries += 1
    
    else:
        print("You have guessed a wrong number! Try Again!!")
        tries += 1